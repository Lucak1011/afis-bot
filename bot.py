# bot.py
import os
import discord
import creds
from dotenv import load_dotenv
from discord.ext import commands
#intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True


# Load the .env file with the token
load_dotenv()
TOKEN = creds.TOKEN

# Create a client instance
client = commands.Bot(command_prefix='!', intents=intents)
@client.event
async def on_ready():
    print("Connected to Discord!")

@client.command()
async def hello(ctx):
    await ctx.send('Hello, I am KetBot!')



# Run the bot
client.run(TOKEN)
