import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from mcstatus import MinecraftServer

load_dotenv()

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
	print('Im Ready')

@bot.command()
async def summon(ctx, arg):
    await ctx.send(arg)

bot.run(os.getenv('TOKEN'))
