import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from mcstatus import MinecraftServer
from datetime import datetime

# TODO:
# - Make bot recover from restart, continuing to edit all existing messages
# - Add configuration to change settings for each specific server, such as time
#   to update message

load_dotenv()

bot = commands.Bot(command_prefix=';', help_command=None)

@bot.event
async def on_ready():
	print('Im Ready')

@bot.command()
async def summon(ctx, arg1, arg2):
	updateMessage = updateMessage = await ctx.send("Fetching server data...")

	while True:
		now = datetime.now()
		currentTime = now.strftime("%B %d, %Y %I:%M:%S %p")
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

		await asyncio.sleep(60)



@bot.command()
async def help(ctx):
	embed=discord.Embed(title="All commands", description='Use the prefix ";" to use them!')
	embed.set_author(name="Version: v1.1.0", url="https://github.com/daniel071/discord-mc-status")
	embed.add_field(name=";summon", value="Makes the bot fetch the server's status and send a contiously updating message", inline=False)
	embed.add_field(name=";config", value="Opens the config menu, where settings can be set", inline=False)
	embed.add_field(name=";help", value="Displays this message", inline=False)
	await ctx.send(embed=embed)


@bot.event
async def on_message(message):
	if bot.user.mentioned_in(message):
		await message.channel.send("You can type `;help` for more info")

	await bot.process_commands(message)


bot.run(os.getenv('TOKEN'))
