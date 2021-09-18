#Fork From @alexdonutz
#Link https://replit.com/@alexdonutz
import discord
import random
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
import os

#-----CLS-----#
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#-----SETUP-----#

client = discord.Client()

prefix = "="


#input token

token = input("Token: ")

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="Myuu Grinder", color=420699, description=f"**{prefix}start**\nAuto Route and fight\n\n**{prefix}stop**\nstops Myuu Grinder\n\n**{prefix}credit**\nShow Credit.")
  await ctx.send('Made By TungMCVN3337#0900',embed=embed)


@bot.command()
async def credit(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="Credit", color=420699, description=f"**@alexdonutz**\nOriginal project - auto dank memer.")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def start(ctx):
	await ctx.message.delete()
	await ctx.send('Successfully enabled Auto Myuu Grinder!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('.route 25')
			await ctx.send(random.randint(1, 4))


@bot.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('Successfully disabled Myuu Grinder!')
	global dmcs
	dmcs = False

clearConsole()

@bot.event
async def on_ready():
  activity = discord.Game(name="Myuu Grinder", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.BLUE}
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

{Fore.GREEN}Grinder is Ready!
Type =help in discord chat for more info.
''')

bot.run(token, bot=False)
