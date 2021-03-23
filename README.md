# Discord Minecraft Status
Discord Minecraft Status is a discord bot with various utilities

## Installation
First, you'll need to create a discord bot and get a token. If you don't know how to, you can use this guide: https://discordpy.readthedocs.io/en/latest/discord.html

You also need to make sure that your minecraft server has `enable-query=true` in the server.properties file and the query port is accessable from the internet.

1. Clone the source code with `git clone https://github.com/daniel071/discord-mc-status.git; cd discord-mc-status`
2. Install required dependencies with `pip install -r requirements.txt`
3. Create a new file called `.env` and add `export TOKEN=(your token here)`
4. Run the program with `python main.py`
