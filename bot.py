import discord
import datetime
import nextcord
import base64
import aiohttp
from io import BytesIO
from nextcord.ext import commands
import time

Intents = discord.Intents.all()

bot = commands.Bot(command_prefix=";", intents=Intents)

@bot.event
async def on_ready():
    print("機器咩咩上班中")

bot.run("TOKEN")