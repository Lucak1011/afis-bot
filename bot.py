# bot.py
import os
import discord
from discord.app_commands import commands
from dotenv import load_dotenv

# Load the .env file with the token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create a client instance
client = commands.Bot(command_prefix='!')

# Define the event
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Run the bot
client.run(TOKEN)
