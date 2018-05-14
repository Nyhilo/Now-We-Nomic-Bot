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

    # Bot should only have read/write permission to these channels
    class CHANNEL:
        inventory = 'turn-order'
        controls = 'bot-control'

    # Format: [Username, Points, {Inventory Dict}]
    playerlist = [  

                    ]


    with open('token.txt','r') as file:
        TOKEN = file.readline()

    client = commands.Bot(command_prefix=PREFIX, description="A bot to manage a whole bunch of things on the Now We Nomic Server")

    # Bot Functions #
    @client.event
    async def on_ready():
        print("Python version", sys.version)
        print('Logged in as', client.user.name)
        print("Discord API version: " + discord.__version__)
        await client.change_presence(game=discord.Game(name='Nomic'))
        await client.send_message(client.get_channel('bot-control'), 'I live!') # <- How to find channel object
        # await client.send_message(discord.Object(CHANNEL.controls), 'I live!')


    @client.command()
    async def hello():
        client.msg = await client.say('Hello World! I am Nwn-bot. Pleased to meet you!')

    @client.command(pass_context=True)
    async def greet(ctx):
        print(ctx.message, ctx.message.channel)
        await client.send_message(ctx.message.channel, "Say hello")
        reply = await client.wait_for_message(author=ctx.message.author, content="hello")   # <- regex goes here
        await client.send_message(ctx.message.channel, "Yo.")


    # # Catch-all for messages.
    # @client.event
    # async def on_message(message):
    #     if message.content.startswith(PREFIX + 'greet'):
    #         await client.send_message(message.channel, 'Say hello')
    #         msg = await client.wait_for_message(author=message.author, content='hello')
    #         await client.send_message(message.channel, 'Hello.')
    #     print(message.author + ": " + message.content)

    client.run(TOKEN)

if __name__ == '__main__':
    print("Please run this bot using init.py.")