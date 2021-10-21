import discord
import random
import time
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive
import os

#-----SETUP-----#
prefix = '='
#use the .env feature to hide your token
intents=discord.Intents.all()
intents.members = True

keep_alive()
token = os.getenv("TOKEN")
bot = commands.Bot(command_prefix=prefix, help_command=None, case_insensitive=True, self_bot=True, intents=intents)

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title=" ", description=" ", color=0xfff700)
  embed.set_author(name="Myuu Grinder Commands", icon_url="https://images.discordapp.net/avatars/438057969251254293/995f42a204040c4ac06d0d0a88976704.png?size=512")
  embed.add_field(name=f"**{prefix}start [route] [move]**", value="Start the grinder", inline=False)
  embed.add_field(name=f"**{prefix}stop**", value="Stop the grinder", inline=False)
  embed.add_field(name=f"**{prefix}teamchecker [minutes]**", value="Check team every minutes", inline=False)
  embed.add_field(name=f"**{prefix}teamoff**", value="Stop the team checker", inline=False)
  embed.add_field(name=f"**{prefix}setup**", value="Show tutorial video to setup myuu", inline=False)
  embed.add_field(name=f"**{prefix}credit**", value="Show Credit", inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def credit(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="tungdo0602", url="https://github.com/tungdo0602", description="Developer")
  embed.set_author(name="Credit", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  await ctx.send(embed=embed)

@bot.command()
async def setup(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="Click Here To See Myuu Grinder Setup Tutorial", url="https://www.youtube.com/watch?v=t1KuIMopoX0", color=0xfff700)
  embed.set_image(url = 'https://img.youtube.com/vi/t1KuIMopoX0/hqdefault.jpg')
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def start(ctx, route: int,move: int):
	await ctx.message.delete()
	if not 1 <= route <= 25:
		await ctx.send('You must choose number between 1 and 25', delete_after=3)
		await ctx.send(f'Usage: {prefix}start route move', delete_after=10)
		return

	if not 1 <= move <= 4:
		await ctx.send('You must choose number between 1 and 4', delete_after=3)
		await ctx.send(f'Usage: {prefix}start route move', delete_after=10)
		return
	await ctx.send('Successfully enabled Auto Myuu Grinder!')
	global mgd
	mgd = True
	while mgd:
		async with ctx.typing():
			await ctx.send(f'.route {route}')
			await asyncio.sleep(1)
			await ctx.send(move)
			await asyncio.sleep(1.35)

@bot.command(pass_context=True)
async def teamchecker(ctx, mins: int):
	await ctx.message.delete()
	await ctx.send('Successfully enabled Auto Team check!')
	global teamon
	teamon = True
	while teamon:
		async with ctx.typing():
			await asyncio.sleep(mins*60)
			await ctx.send('.team')

@bot.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('Successfully disabled Myuu Grinder!')
	global mgd
	mgd = False

@bot.command()
async def teamoff(ctx):
	await ctx.message.delete()
	await ctx.send('Successfully disabled Team Checker!')
	global teamon
	teamon = False

async def on_message(ctx, msg, message):
  if ":" == msg.content[0] and ":" == msg.content[-1]:
    emoji_name = msg.content[1:-1]
    for emoji in msg.guild.emojis:
      if emoji_name == emoji_name:
        await msg.channel.send(str(emoji))

@bot.event
async def on_ready():
  activity = discord.Activity(type=discord.ActivityType.watching, name="YOU!")
  await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
  
  print(f'''
{Fore.BLUE}
███╗░░░███╗██╗░░░██╗██╗░░░██╗██╗░░░██╗
████╗░████║╚██╗░██╔╝██║░░░██║██║░░░██║
██╔████╔██║░╚████╔╝░██║░░░██║██║░░░██║
██║╚██╔╝██║░░╚██╔╝░░██║░░░██║██║░░░██║
██║░╚═╝░██║░░░██║░░░╚██████╔╝╚██████╔╝
╚═╝░░░░░╚═╝░░░╚═╝░░░░╚═════╝░░╚═════╝░
░██████╗░██████╗░██╗███╗░░██╗██████╗░███████╗██████╗░
██╔════╝░██╔══██╗██║████╗░██║██╔══██╗██╔════╝██╔══██╗
██║░░██╗░██████╔╝██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██║░░╚██╗██╔══██╗██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║██║░╚███║██████╔╝███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
''')

bot.run(token, bot=False)
