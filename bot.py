from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
import scripts
import asyncio
import ffmpeg


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


@bot.tree.command(name="search",
                  description="""Searches minecraft.wiki for basic information about a specific block.""",
                  guild=discord.Object(id=server_token)
                  )

async def search(ctx, item_name: str):
    item_data = scripts.wiki_scrape(item_name)
    if item_data["error"]:
        await ctx.response.send_message(f"{item_data["item_name"].replace("+", " ").title()} was not found!", ephemeral=True)
    else:
        embed=discord.Embed(title=item_data["title"], url=item_data["url"], description=item_data["description"])
        embed.set_thumbnail(url=item_data["image"])
        await ctx.response.send_message(embed=embed)


@bot.tree.command(name="waypoint",
                  description="""Accepts a location name and coordinates and sends a formatted message to the coordinates chat.""",
                  guild=discord.Object(id=server_token)
                  )

async def waypoint(ctx, location_name: str, x_coord: str, y_coord: str, z_coord: str, nether: bool):
    if nether:
        channel = bot.get_channel(1194042960958988319)
        channel_name = "nether_coords"
    else:
        channel = bot.get_channel(1166879806793732180)
        channel_name = "cool_coords"
    
    await channel.send(f"""
# {location_name.title()}
`{x_coord} / {y_coord} / {z_coord}`""")
    await ctx.response.send_message(f"Coordinates saved in {channel_name}!", ephemeral=True)


@bot.tree.command(name="quack",
                  description=":)",
                  guild=discord.Object(id=server_token)
                  )

async def quack(ctx):
    try:
        voice_channel = ctx.user.voice.channel
    except AttributeError:
        await ctx.response.send_message("You're not in a voice channel!", ephemeral=True)
        return None
    await ctx.response.send_message("Q U A C K", ephemeral=True)
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio(source="quack.mp3", executable="ffmpeg/bin/ffmpeg.exe"), after=lambda e: print("LATER", e))
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()


bot.run(token)
