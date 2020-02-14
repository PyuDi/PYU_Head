from discord.ext import commands

import discord
from calc import calc
import randomize

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
	async def c(self, ctx, p, g, b, m, tp):
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
		usage='[all/free/bm/capso / paff/neko/robo/ivy/cp / miku/xenon/conner/cherry/joe/rin/sagar/aroma/nora/nekopunk / glitch / 15 / 14]'
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


def setup(bot):
    bot.add_cog(Cytus(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
