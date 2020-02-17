from bs4 import BeautifulSoup 
from fuzzywuzzy import fuzz
from pykakasi import kakasi
from collections import Counter

import requests
import pandas as pd
import re
import numpy as np
import discord
#
import lxml
#

#################################################

source = "https://ct2view.the-kitti.com/chartlist.html"
prefix = "https://ct2view.the-kitti.com"

# initialized settings for pykakasi module
kakasi = kakasi()
kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
kakasi.setMode("J","a") # Japanese to ascii, default: no conversion
kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
kakasi.setMode("s", True) # add space, default: no separator
kakasi.setMode("C", False) # capitalize, default: no capitalize
conv = kakasi.getConverter()

# regex to detect Japanese characters + Kanji
jpregex = re.compile('[\u4E00-\u9FAF]|[\u3000-\u303F]|[\u3040-\u309F]|\
                    [\u30A0-\u30FF]\|[\uFF00-\uFFEF]|[\u4E00-\u9FAF]|\
                    [\u2605-\u2606]|[\u2190-\u2195]|\u203B')

# regex to detect emotes in user input
emoteregex = re.compile("(:[a-zA-Z0-9_\-~]+?:)")

# regex to detect pings, channel titles, or roles
pingregex = re.compile("<(#|@!|@#)\d+>")

# regex to detect which difficulty a link corresponds to
regex_by_diff = [re.compile("chartlist\/(.*?)\/easy"),
                re.compile("chartlist\/(.*?)\/hard"),
                re.compile("chartlist\/(.*?)\/chaos"),
                re.compile("chartlist\/(.*?)\/glitch")]

difficulties = ["easy.html", "hard.html", "chaos.html", "glitch.html"]

regex_dict = dict(zip(difficulties, regex_by_diff))

#################################################

def get_table(source):
    """
    Scrapes the main table from the ct2viewer website. 
    Used for grabbing song links since pd.html doesn't also scrape hyperlinks.
    
    :param source: ct2viewer site link
    :return: HTML table
    """

    try:
        r = requests.get(source)
        c2v = BeautifulSoup(r.content, features = 'lxml')
        table = c2v.body.table.tbody

        return table
    
    except:
        return Exception("Unable to request from page.")

def get_initial_df(source):
    """
    Reads all relevant information from the site to a dataframe.

    :param source: ct2viewer site link
    :return: pandas DataFrame object containing information such as song titles,
            artist names, difficulties, BPMs and so on.
    """ 

    charts_df = pd.read_html(source, encoding = "UTF-8")
    charts_df = pd.concat(charts_df)
    charts_df.rename(columns = {"Lv.":"Diff_E","Lv..1":"Diff_H",
        "Lv..2":"Diff_C","Lv..3":"Diff_G"
        ,"Chart":"Chart_E","Chart.1":"Chart_H"
        ,"Chart.2":"Chart_C","Chart.3":"Chart_G"}, inplace = True)

    return charts_df

#################################################

def get_links_by_difficulty(table):
    """
    Formats all links from the HTML table obtained earlier and puts them
    into a dictionary.

    :param table: HTML table
    :return: Dictionary in the format: {<difficulty> : [list of <links>]}
    """

    links = [link.get('href') for link in table.find_all('a')]
    linksFormatted = [f"{link}.html" for link in links]
    links_dict = {diff: [link for link in linksFormatted if diff in link] for diff in difficulties}

    return links_dict
    

def get_keys_by_difficulty(links_dict):
    """
    All songs from the site are formatted in this manner:
    https://ct2view.the-kitti.com/chartlist/<song identifier>/<difficulty>

    This function returns all unique song identifiers (keys) present for 
    each difficulty using the regexes from earlier.

    :param links_dict: Dictionary of links by difficulty
    :return: Dictionary in the format: {<difficulty> : [list of <keys>]}
    """

    keys_dict = dict()
    for diff in difficulties:
        result = [" ".join(key.split("_")) for link in links_dict[diff] 
                        for key in regex_dict[diff].findall(link)]
        keys_dict[diff] = result

    return keys_dict

def merge_keys_and_links(table):
    """
    Helper function. Merges links_dict and keys_dict

    :param table: HTML table scraped from site
    :return: Dictionary of dictionaries in the format: 
            {<difficulty> : [list of dictionaries {<key> : <link>}]}
    """

    links_dict = get_links_by_difficulty(table)
    keys_dict = get_keys_by_difficulty(links_dict)

    merged_dict = {k: dict(zip(keys_dict[k], links_dict[k])) for k in keys_dict}
    return merged_dict

#################################################

def merge_data(charts_df, merged_dict):
    """
    Create a new DataFrame object containing song keys to be merged with
    the original DataFrame.

    :param charts_df: Original DataFrame containing information about each
                      chart, excluding unique song keys.
    :param merged_dict: Dictionary of dictionaries previously obtained
                        containing difficulties and their corresponding
                        keys/links.

    :return: New DataFrame now with each song's corresponding unique key. 
    """

    # all unique keys are present only for CHAOS difficulty since the site
    # does not include most EASY/HARD difficulty views
    links_df = pd.DataFrame({
                            'Song' : charts_df.Song, 
                            'Artist' : charts_df.Artist, 
                            'Key' : list(merged_dict['chaos.html'].keys()), 
                            })

    merged_df = pd.merge(left = charts_df, right = links_df, 
                        left_on = ['Song', 'Artist'], 
                        right_on = ['Song', 'Artist'])

    return merged_df

def get_romanized_titles(merged_df):
    """
    Create new column in the DataFrame for ONLY Japanese-titled songs
    containing the romanized title of the song obtained from pykakasi.

    :param merged_df: Merged DataFrame containing all relevant song info
    :return: Same DataFrame but now with romanized titles
    """

    for song in merged_df.Song:
        if jpregex.findall(song):
            merged_df.loc[merged_df.Song == song, 'Key_J'] = conv.do(song)

        else: 
            # fill other rows with whitespace as opposed to NaN by default
            merged_df.loc[merged_df.Song == song, 'Key_J'] = ""

    return merged_df

def handle_duplicates(merged_df):
    """
    Pre-processing function to handle songs that have identical titles.
    :param merged_df: DataFrame containing all relevant song info
    :return: Same DataFrame but with duplicate song titles being in the
            format Song (Artist)
    """

    if (duplicated := merged_df.duplicated(subset = ['Song'])).any():
        song_duplicates = list(merged_df[duplicated].to_records())
        
        for dupe in song_duplicates:
            indexes = merged_df.index[merged_df.Song == dupe.Song].tolist()

        for index in indexes:
            merged_df.loc[index, 'Song'] += f" ({merged_df.loc[index].Artist})"
            
    return merged_df

def get_merged_df(charts_df, merged_dict):
    """
    Helper function to obtain and perform all necessary preprocessing steps on 
    the merged DataFrame.

    :param charts_df: Original DataFrame containing information about each
                      chart, excluding unique song keys.
    :param merged_dict: Dictionary of dictionaries previously obtained
                        containing difficulties and their corresponding
                        keys/links.
    :return: Final merged DataFrame containing unique keys, romanized keys 
            for songs with Japanese titles, and duplicates handled accordingly.
    """

    merged_df = merge_data(charts_df, merged_dict)
    merged_df = get_romanized_titles(merged_df)
    merged_df = handle_duplicates(merged_df)

    return merged_df

#################################################

def compare_fuzz(song, best_matches, best_fuzz_ratio, fuzz_value):
    """
    compare_fuzz: A helper function to compare fuzz values then add it to the best_matches array, if needed
    :param song: The song to potentially add
    :param best_matches: A list of best matches
    :param best_fuzz_ratio: The currently best fuzz ratio
    :param fuzz_value: Fuzz ratio of the song compared to user's query
    :return: True if the fuzz_ratio was better and needs to be updated
             False if the fuzz_ratio does not need to be modified
    """

    # If fuzz_value is greater than best_fuzz ratio, set best to fuzz_value and set best_matches to only that song
    if fuzz_value > best_fuzz_ratio:
        best_matches.clear()
        best_matches.append(song)
        return True

    # Otherwise, if fuzz and best are equal, add the song to the list
    elif fuzz_value == best_fuzz_ratio:
        best_matches.append(song)
        return False

    return False


def search_song(df, query):
    """
    search_song: Fetches the closest matching song from the database
                    - If multiple are found, return a list of potential songs
    :param df: DataFrame object to obtain info of search result
    :param query: A query in string format, usually the name of a song
    :return: DataFrame object containing all information about the song
    """

    # Checks for song list iteration
    is_japanese = re.search(jpregex, query) is not None

    # Keep track of "best" matches and ratios
    best_fuzz_ratio = 0
    best_matches = []
    
    for index, row in df.iterrows():
        if is_japanese:
        
            if row.Song.lower() == query.lower():
                return df.loc[df.Song == row.Song]

            # compare to the Song attribute since it's the only column
            # with Japanese titles

            fuzz_value = fuzz.token_set_ratio(row.Song, query)

            if compare_fuzz(row, best_matches, best_fuzz_ratio, fuzz_value):
                best_fuzz_ratio = fuzz_value


        else:

            if row.Song.lower() == query.lower():
                return df.loc[df.Song == row.Song]

            """
            have to compare to 3 attributes:
            1) Song for English titles

            2) Key also for English titles. 

            Guards against three edge cases:
            Works better if user input is the translated title of the song
            (e.g. the key for the song 鬲疲ｳ輔∩縺溘＞縺ｪ繝溘Η繝ｼ繧ｸ繝�繧ｯ�ｼ� is music_like_magic)
            or if song contains special characters
            (e.g. key for Re:VeLﾎ乃iﾃ朗 �ｽ槫�蛾％繝育�ｴ螢翫ヮ蜿檎區鄙ｼ�ｽ� is revelation)
            or song title is actually in Chinese, including dialects
            (e.g. key for 荳蝠門�ｩ蝠� is yaat_daam_loeng_daam)

            3) Key_J if user input is romanized Japanese.
            Guards against edge case if the song title is actually in 
            Chinese but user inputs romanized Japanese instead:
            (e.g. user inputs ichi tan ryou tan instead of yaat daam loeng daam for 荳蝠門�ｩ蝠�)
            """
            fuzz_value = fuzz.token_set_ratio(row.Song, query)
            fuzz_value_key = fuzz.token_set_ratio(row.Key, query)
            fuzz_value_romanized = fuzz.token_set_ratio(row.Key_J, query)

            if compare_fuzz(row, best_matches, best_fuzz_ratio, fuzz_value):
                best_fuzz_ratio = fuzz_value

            if compare_fuzz(row, best_matches, best_fuzz_ratio, fuzz_value_key):
                best_fuzz_ratio = fuzz_value_key
            
            if compare_fuzz(row, best_matches, best_fuzz_ratio, fuzz_value_romanized):
                best_fuzz_ratio = fuzz_value_romanized

    if best_fuzz_ratio == 0:
        return []

    # removes duplicates from search
    songs = set([song.Song for song in best_matches])
    output = [df.loc[df.Song == song] for song in songs]
    print(output)
    return pd.concat(output)


def search_difficulty(df, query):
    output = []

    for index, row in df.iterrows():
        if (row.Diff_E == query or row.Diff_H == query 
            or row.Diff_C == query or row.Diff_G == query):
            
            output.append(row.Song)

    partitioned_output = [output[i : i + 6] for i in range(0, len(output), 6)]
    print(partitioned_output)

    return partitioned_output

#################################################

def get_images(link):
    """
    Gets the song artwork and character logo from the link of a song.
    :param link: Link to scrape thumbnail from
    :return: Link to artwork and logo in proper format
    """

    r = requests.get(link)
    page = BeautifulSoup(r.content, features = 'lxml')
    images = page.find_all('img')

    artwork = "".join(image['src'] for image in images if 'thumbnail' in image['src'])

    if (root := "../..") in artwork:
        artwork = artwork.replace(root, prefix)
    else:
        artwork = prefix + artwork

    return artwork

def embed_song(merged_dict, song):
    """
    Outputs details of a song including the song's title, its artist, BPM
    and hyperlinks to each of its (available) charts.
    :param merged_dict: Dictionary to find a chart's links
    :return: Formatted discord.Embed object
    """
    
    song = song.to_records()
    
    # obtain all available links to song
    links = [merged_dict[diff].get("".join(song.Key)) for diff in difficulties]

    # since each song is guaranteed to have a CHAOS chart on the site
    # grab the thumbnail from the CHAOS link
    artwork = get_images(links[2])

    print(links)

    embed = discord.Embed(title = f'{"".join(song.Song)}', color = 0x1abc9c)
    embed.set_thumbnail(url = artwork)

    embed.add_field(name = "Artist", value = f'{"".join(song.Artist)}', inline = False)
    embed.add_field(name = "BPM", value = f'{"".join(song.BPM)}', inline = True)
    embed.add_field(name = "Character", value = f'{"".join(song.Character)}', inline = True)

    difficulty_string = ""

    # obtain links and output in discord hyperlink format, i.e.
    # [text here](url here)
    if links[0] is not None:
        difficulty_string += f'[EASY {"".join(str(int(song.Diff_E)))}]({links[0]})'
        difficulty_string += " | "
    
    if links[1] is not None:
        difficulty_string += f'[HARD {"".join(str(int(song.Diff_H)))}]({links[1]})'
        difficulty_string += " | "
        
    difficulty_string +=  f'[CHAOS {"".join(str(int(song.Diff_C)))}]({links[2]})'

    if links[3] is not None:
        difficulty_string += " | "
        difficulty_string += f'[GLITCH {"".join(str(int(song.Diff_G)))}]({links[3]})'

    embed.add_field(name = "Difficulty", value = difficulty_string, inline = False)
        
    return embed

def process_search(merged_dict, search_result):
    """
    Helper function. Returns different outputs depending on the search result.
    :param merged_dict: Dictionary to obtain song links from
    :param search_result: Result of the function search_song
    :return: Appropriate discord.Embed object
    """

    if len(search_result) == 0:
        embed = discord.Embed(title = 'Error', color = 0x992d22,
                            description = """No songs found. There could be an error with
                                your search or the bot.""")
    
        return embed

    elif len(search_result) == 1:
        return embed_song(merged_dict, search_result)
        
    elif len(search_result) > 1:
        results = [row.Song for index, row in search_result.iterrows()]

        embed = discord.Embed(title = 'Error', color = 0x992d22,
                            description = """Too many songs found. Please enter
                            a song from the list given.""" + "\r\n" + "\r\n".join(results))
        
        return embed