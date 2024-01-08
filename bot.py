from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
import scripts


# initializing bot, command tree, and tokens
load_dotenv()
token = os.getenv("discord_token")
server_token = os.getenv("minecraft_server_token")
bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())


# bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=server_token))
    print(f"{bot.user} is quacking!")

@bot.tree.command(
    name="search",
    description="""Searches minecraft.wiki for basic information about a specific block.
    Usage: /search [item name]""",
    guild=discord.Object(id=server_token)
)
async def search(ctx, item_name: str):
    item_data = scripts.wiki_scrape(item_name)
    if item_data["error"]:
        await ctx.response.send_message("Item not found!")
    else:
        embed=discord.Embed(title=item_data["title"], url=item_data["url"], description=item_data["description"])
        embed.set_thumbnail(url=item_data["image"])
        await ctx.response.send_message(embed=embed)

bot.run(token)
