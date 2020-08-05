from discord.ext import commands

import discord
from calc import calc
import randomize
import search
import re

class Cytus(commands.Cog):
    
	def __init__(self, bot):
		self.bot = bot

  # Define a new command
	@commands.command(
		name='c',
		description='Calculates number of wps',
		aliases=['calc','calculate'],
		usage='[perfect] [good] [bad] [miss] [tp]'
	)
	async def c(self, ctx, p="0", g="0", b="0", m="0", tp="0.0"):
		res = calc(p, g, b, m, tp)
		embed = discord.Embed(title="?c"+" "+p+" "+g+" "+b+" "+m+" "+tp, description="", color=0xccc481)
		embed.set_footer(
    		text=f'Requested by {ctx.message.author.name}',
    		icon_url=ctx.message.author.avatar_url
    	)
		embed.add_field(name="Result", value=res, inline=False)
		await ctx.send(embed=embed)

		return

	###

	@commands.command(
		name='r',
		description='Randomizes Cytus 2 songs :game_die:',
		aliases=['rand','randomize'],
		usage='[all/free/bm/capso / paff/neko/robo/ivy/cp/vanessa / miku/xenon/conner/cherry/joe/rin/sagar/aroma/nora/nekopunk / glitch / 15 / 14]'
	)
	async def r(self, ctx, selection="all"):
		title = "Result"
		res = randomize.rand(selection)
		if (selection=="graff" or selection=="graffj"):
			title = "Well,"
		embed = discord.Embed(title="?r "+str(selection), description="", color=0x81ccc4)
		embed.set_footer(
      		text=f'Requested by {ctx.message.author.name}',
      		icon_url=ctx.message.author.avatar_url
    	)
		embed.add_field(name=title, value=res, inline=False)
		await ctx.send(embed=embed)

		return
	
	###

	# initializing dataframe used for searching songs and dictionary for storing links
	table = search.get_table(search.source)
	charts_df = search.get_initial_df(search.source)

	merged_dict = search.merge_keys_and_links(table)
	merged_df = search.get_merged_df(charts_df, merged_dict)

	@commands.command(
		name='s',
		description='Searches Song Charts from ct2view :heart:',
		aliases=['search','find'],
		usage='[song name]'

	)
	async def s(self, ctx, *, arg):
		"""
    	Searches ct2viewer for a song that matches closest to the user input.
    	Returns an embed containing the song information and links to its charts.
    	"""
		channel = ctx.channel

		is_emote = re.search(search.emoteregex, arg) is not None
		is_ping = re.search(search.pingregex, arg) is not None

		if is_emote or is_ping:
			embed = discord.Embed(title = 'Error', color = 0x992d22,
                description = 'Invalid input. Emote, ping, or channel name detected.')

			await channel.send(embed = embed)
			return

		result = search.search_song(Cytus.merged_df, arg)
		embed = search.process_search(Cytus.merged_dict, result)
		embed.set_footer(
    		text=f'Requested by {ctx.message.author.name}',
    		icon_url=ctx.message.author.avatar_url
    	)


		await channel.send(embed = embed)

	@s.error 
	async def s_error(self, ctx, error):
		"""
		Error handler in case user forgets to specify the search key.
		"""
		if isinstance(error, commands.MissingRequiredArgument):
			embed = discord.Embed(title = 'Error', color = 0x992d22,
                description = "Please also specify a search key.")
			embed.set_footer(
    			text=f'Requested by {ctx.message.author.name}',
    			icon_url=ctx.message.author.avatar_url
    		)
    
			await ctx.send(embed = embed)

			return


def setup(bot):
    bot.add_cog(Cytus(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
