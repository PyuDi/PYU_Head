from discord.ext import commands
# Import the keep alive file
import keep_alive
import os
import replit
import discord

###########
from calc import calc
import randomize
###########


def get_prefix(client, message):

    prefixes = ['??']    # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['??']   # Only allow '==' as a prefix when in DMs

    # Allow users to @mention the bot instead of using a prefix when using a command.
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(                                         
    # Create a new bot
    command_prefix=get_prefix,                              # Set the prefix
    description='PYU_Head',                  # Set a description for the bot
    owner_id=408795307296423942,                            # Your unique User ID
    case_insensitive=False                                   # Make the commands case insensitive
)

# case_insensitive=True is used as the commands are case sensitive by default

# cogs = ['cogs.basic','cogs.embed']
cogs = []


@bot.event
async def on_ready():
		replit.clear()
		print(f'Logged in as {bot.user.name} - {bot.user.id}')
    # bot.remove_command('help')
    # Removes the help command
    # Make sure to do this before loading the cogs
		for cog in cogs:
				bot.load_extension(cog)
		activity = discord.Game(name="& Waiting for ??helpme")
		await bot.change_presence(status=discord.Status.online, activity=activity)
		return

####################
@bot.command()
async def helpme(ctx):
		embed = discord.Embed(title="LIST OF COMMANDS", description="", color=0xcccccc)
		embed.add_field(name="List", value="  **??r [char]** : randomizes song \n **??rhelp** : ??r help \n **??c [p g b m tp]** : calculates the number of lemon perfects \n **??chelp** : ??c help \n\n **??about** : about the bot \n **??helpme** : shows this", inline=False)
		await ctx.channel.send(embed=embed)


@bot.command()
async def test(ctx):
    await ctx.send(">>> YAMAMETO!")

@bot.command()
async def chelp(ctx):
		title = "How to Use"
		res = "**??c [# of perfect] [# of good] [# of bad] [# of miss] [tp]**\n substitute every brackets"
		embed = discord.Embed(title="??chelp", description="Cytus TP Calculator HELP", color=0xccc481)
		embed.add_field(name=title, value=res, inline=False)
		await ctx.channel.send(embed=embed)

@bot.command()
async def c(ctx, p, g, b, m, tp):
		res = calc(p, g, b, m, tp)
		embed = discord.Embed(title="??c", description="Cytus TP Calculator", color=0xccc481)
		embed.add_field(name="Result", value=res, inline=False)
		await ctx.channel.send(embed=embed)

@bot.command()
async def rhelp(ctx):
		title = "List of Commands"
		res = "**all / free** \n paff / neko / robo / ivy / cp \n miku / xenon / conner / cherry / joe / rin / sagar \n aroma / nora / nekopunk"
		embed = discord.Embed(title="??rhelp", description="Cytus 2 Song Randomizer HELP", color=0x81ccc4)
		embed.add_field(name=title, value=res, inline=False)
		await ctx.channel.send(embed=embed)

@bot.command()
async def r(ctx,selection):
		res = ""
		title = "Result"
		if (str(selection)=="all"):
			res = randomize.f_allchar()
		elif (str(selection)=="free"):
			res = randomize.f_free()
		
		elif (str(selection)=="paff"):
			res = randomize.f_paff()
		elif (str(selection)=="neko"):
			res = randomize.f_nekow()
		elif (str(selection)=="robo"):
			res = randomize.f_robohead()
		elif (str(selection)=="ivy"):
			res = randomize.f_ivy()
		elif (str(selection)=="cp"):
			res = randomize.f_cp()

		elif (str(selection)=="miku"):
			res = randomize.f_miku()
		elif (str(selection)=="xenon"):
			res = randomize.f_xenon()
		elif (str(selection)=="conner"):
			res = randomize.f_conner()
		elif (str(selection)=="cherry"):
			res = randomize.f_cherry()
		elif (str(selection)=="joe"):
			res = randomize.f_joe()
		elif (str(selection)=="sagar"):
			res = randomize.f_sagar()
		elif (str(selection)=="rin"):
			res = randomize.f_rin()

		elif (str(selection)=="aroma"):
			res = randomize.f_aroma()
		elif (str(selection)=="nora"):
			res = randomize.f_nora()
		elif (str(selection)=="nekopunk"):
			res = randomize.f_neko()

		embed = discord.Embed(title="??r", description="Cytus 2 Song Randomizer", color=0x81ccc4)
		embed.add_field(name=title, value=res, inline=False)
		await ctx.channel.send(embed=embed)

@bot.command()
async def about(ctx):
		embed = discord.Embed(title="PYU_Head V2.0", description="made by H8v_PyuDi#7059", color=0xcccccc)
		embed.add_field(name="Info", value="Last Updated : 200210 \nSongs : up to v2.8.5 \n\nPM H8v_PyuDi#7059 for Bot Invite Link", inline=False)
		await ctx.channel.send(embed=embed)


####################

# Start the server
keep_alive.keep_alive()

# Finally, login the bot
bot.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
