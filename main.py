import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from mcstatus import MinecraftServer
from datetime import datetime

# TODO:
# Make bot recover from restart, continuing to edit all existing messages
# Add readme
# Add help command

load_dotenv()

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
	print('Im Ready')

@bot.command()
async def summon(ctx, arg1, arg2):
	updateMessage = updateMessage = await ctx.send("Fetching server data...")

	while True:
		now = datetime.now()
		currentTime = now.strftime("%B %d, %Y %H:%M:%S")
		server = MinecraftServer.lookup("{ip}:{port}".format(ip=arg1, port=arg2))
		try:
			status = server.status()
			query = server.query()

			message = """
			**Current Server Status**
			(last updated {time})
			Server online: :white_check_mark:
			Latency: **{latency}ms**
			Players online: **{players_online}**
			Current players: {players_list}
			""".format(time=currentTime, latency=status.latency, players_online=status.players.online, players_list=", ".join(query.players.names))
		except ConnectionRefusedError:
			message = """
			**Current Server Status**
			(last updated {time})
			Server online: :x:
			""".format(time=currentTime)

		try:
			await updateMessage.edit(content=message)
		except discord.NotFound:
			break

		await asyncio.sleep(5)
		print("update completed")



bot.run(os.getenv('TOKEN'))
