# bot.py
import os
import discord
from dotenv import load_dotenv

# Load the .env file with the token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create a client instance
client = discord.Client()

# Define the event
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Run the bot
client.run(TOKEN)
