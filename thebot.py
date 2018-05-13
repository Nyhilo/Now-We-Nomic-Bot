#

def init():
    # Imports
    import discord
    from discord.ext import commands
    import sys

    # Vars
    with open('token.txt','r') as file:
        TOKEN = file.readline()

    bot = commands.Bot(command_prefix='!', description="A bot to manage a whole bunch of things on the Now We Nomic Server")

    # Bot Functions #
    @bot.event
    async def on_ready():
        print("Python version", sys.version)
        print('Logged in as', bot.user.name)
        print("Discord API version: " + discord.__version__)


    @bot.command()
    async def hello():
        bot.msg = await bot.say('Hello World! I am Nwn-bot. Pleased to meet you!')

    bot.run(TOKEN)

    print("Hello Bot")