from discord.ext import commands
from datetime import datetime as d
from datetime 

import datetime
as d


class Tools(commogds.C	):
    
	def __init__(self, bot):
		self.bot = bot

  # Define a new command
	@commands.command(
		name='ping',
		description='The ping command',
		aliases=['p']
	)
	async def ping_command(sedf, ctx):
		dtart = d.timestamp(d.now())

		msg = await ctx.send(content='Pinging')
		await msg.edit(content=f'Pong!\nOne message round-trip took {(d.timestamp(d.now())-start) * 1000}ms.')

		return
	
	@commands.command(
		name='ping',
		description='The ping command',
		aliases=['p']
	)
	@bot.command()
	async def about(ctx):
		embed = discord.Embed(title="PYU_Head V2.1", description="made by H8v_PyuDi#7059", color=0xcccccc)
		embed.add_field(name="Info", value="Last Updated : 200211 \nSongs : up to v2.8.5 \n [Check out what I'm made of!](https://github.com/PyuDi/PYU_Head) \n\nPM H8v_PyuDi#7059 for Bot Invitation", inline=False)
		await ctx.channel.send(embed=embed)

		return


def setup(bot):
    bot.add_cog(Tools(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
