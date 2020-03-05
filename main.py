from discord.ext import commands
# Import the keep alive file
import keep_alive
import os
import replit
import discord



def get_prefix(client, message):

    prefixes = ['?', ',']    # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['?']   # Only allow '?' as a prefix when in DMs

    # Allow users to @mention the bot instead of using a prefix when using a command.
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(                                         
  # Create a new bot
  command_prefix=get_prefix,
	# Set the prefix
  description='PYU_Head',
	# Set a description for the bot
  owner_id=408795307296423942,
	# Your unique User ID
  case_insensitive=True
	# Make the commands case insensitive
)

# case_insensitive=True is used as the commands are case sensitive by default

cogs = ['cogs.cytus','cogs.tools']


@bot.event
async def on_ready():
	replit.clear()
	print(f'Logged in as {bot.user.name} - {bot.user.id}')
	bot.remove_command('help')
	for cog in cogs:
		bot.load_extension(cog)
	activity = discord.Game(name="Cytus II & Waiting ?help")
	await bot.change_presence(status=discord.Status.online,activity=activity)
	return

####################

@bot.command()
async def test(ctx):
  await ctx.send(">>> YAMAMETO!")

# https://discordapp.com/oauth2/authorize?scope=bot&client_id=676146100721156096
####################

# Start the server
keep_alive.keep_alive()

# Finally, login the bot
bot.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
