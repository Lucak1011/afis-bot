# bot.py
import os
import discord
from dotenv import load_dotenv # type: ignore
from discord.ext import commands
#intents
intents = discord.Intents.all()
intents.messages = True
intents.guilds = True


# Load the .env file with the token
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# Create a client instance
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("Connected to Discord!")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am KetBot!")

@client.command()
async def bigLL26l(ctx):
    await ctx.send("“[Callsign], cleared to [Dest] via Biggin, after departure runway 26L/R climb straight ahead to I-WW 2.3 DME, then turn right heading 075, climb to altitude 4000 ft, speed 220 knots or less, squawk [Code].”")



# Run the bot
client.run(TOKEN)
