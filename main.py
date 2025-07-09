import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("¡Pong!")

bot.run(os.getenv("MTM4ODM2MTQyNzM5OTc0MTUyMA.Gtg7lF.JeXRSyvUHn2DpTZpNo7VNC_mRuht1T1kdgynms"))
