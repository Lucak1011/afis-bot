#bot.py
import os
import discord


TOKEN = os.environ['MTI1NzM4MjQ1MzU4OTMxNTY0NA.Gmc9ZG.gFxGuZVPEc8mdGap_lDYCgJ7C0kGeKxVXURq-Y']
client = discord.Client()
from dotenv import load_dotenv
@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')
client.run(TOKEN)