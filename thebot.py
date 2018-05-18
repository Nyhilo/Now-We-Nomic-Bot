#

def init():
    # Imports
    import discord
    from discord.ext import commands
    import sys

    # Local imports
    import point_management
    import events

    # Vars #
    PREFIX = '!'
    client = commands.Bot(command_prefix=PREFIX, description="A bot to manage a whole bunch of things on the Now We Nomic Server")

    with open('token.txt','r') as file:
        TOKEN = file.readline()

    # Bot should only have read/write permission to these channels
    class CHANNEL:
        inventory = '445373512471805953'
        controls = '445377007547580424'


    # Bot Functions #
    @client.event
    async def on_ready():
        print("Python version", sys.version)
        print('Logged in as', client.user.name)
        print("Discord API version: " + discord.__version__)
        await client.change_presence(game=discord.Game(name='Nomic'))

    # Example command
    @client.command()
    async def hello():
        client.msg = await client.say('Hello World! I am Nwn-bot. Pleased to meet you!')
        await client.send_message(client.get_channel(CHANNEL.controls), 'I live!')

    # Example Call and Response
    @client.command(pass_context=True)
    async def greet(ctx):
        print(ctx.message, ctx.message.channel)
        await client.send_message(ctx.message.channel, "Say hello")
        reply = await client.wait_for_message(author=ctx.message.author, content="hello")   # <- regex goes here
        await client.send_message(ctx.message.channel, "Yo.")

    client.run(TOKEN)

if __name__ == '__main__':
    print("Please run this bot using init.py.")
