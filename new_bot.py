from discord.ext import commands
import discord
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("discord_token")
server_token = os.getenv("server_token")
bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"{bot.user} is quacking!")


@bot.command()
async def hello(ctx):
    await ctx.send("What's up playa?")


bot.run(token)
