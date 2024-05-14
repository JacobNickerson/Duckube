from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
import scripts
import asyncio
import subprocess


# initializing bot, command tree, and tokens
load_dotenv(override=True)
token = os.getenv("discord_token")
server_token = os.getenv("discord_server_token")
admin = os.getenv("owner_token")
bot = commands.Bot(command_prefix="/", intents=discord.Intents.default(), owner_id=admin)
mods_directory = os.getenv("mods_directory")
Guild = discord.Object(id=server_token)
p = None


# bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync(guild=Guild)
    print(f"{bot.user} is quacking!")


@bot.tree.command(name="search",
                  description="""Searches minecraft.wiki for basic information about a specific block""",
                  guild=Guild
                  )
async def search(ctx, item_name: str):
    item_data = scripts.wiki_scrape(item_name)
    if item_data["error"]:
        await ctx.response.send_message(f"Nothing was found for: {item_name}", ephemeral=True)
        #await ctx.response.send_message(f"{item_data["item_name"].replace("+", " ").title()} was not found!", ephemeral=True)
    else:
        embed=discord.Embed(title=item_data["title"], url=item_data["url"], description=item_data["description"])
        embed.set_thumbnail(url=item_data["image"])
        await ctx.response.send_message(embed=embed)


@bot.tree.command(name="waypoint",
                  description="""Accepts a location name and coordinates and sends a formatted message to the coordinates chat""",
                  guild=Guild
                  )
async def waypoint(ctx, location_name: str, x_coord: str, y_coord: str, z_coord: str):
    channel = bot.get_channel(int(os.getenv("coords_channel_id")))
    channel_name = "coordinates"
    
    await channel.send(f"""
# {location_name.title()}
`{x_coord} / {y_coord} / {z_coord}`""")
    await ctx.response.send_message(f"Coordinates saved in {channel_name}!", ephemeral=True)


@bot.tree.command(name="quack",
                  description=":)",
                  guild=Guild
                  )
async def quack(ctx, count: int=1):
    try:
        voice_channel = ctx.user.voice.channel
    except AttributeError:
        await ctx.response.send_message("You're not in a voice channel!", ephemeral=True)
        return None
    global vc
    vc = await voice_channel.connect()
    await ctx.response.send_message("Q U A C K", ephemeral=True)
    for _ in range(0,count):
            vc.play(discord.FFmpegPCMAudio(source="quack.mp3", executable="ffmpeg/bin/ffmpeg.exe"))
            while vc.is_playing():
                await asyncio.sleep(1)
    await vc.disconnect()


@bot.tree.command(name="silence",
                  description="Silences the quacks", 
                  guild=Guild
                  )
async def silence(ctx):
    try:
        if vc.is_playing():
            await vc.disconnect()
            await ctx.response.send_message("Sorry...", ephemeral=True)
        else:
            await ctx.response.send_message("I'm not quacking right now.", ephemeral=True)
    except NameError:
        await ctx.response.send_message("I'm not quacking right now.", ephemeral=True)


@bot.tree.command(name="start_server", 
                  description="Starts the server", 
                  guild=Guild
                  )
@discord.app_commands.checks.has_permissions(administrator = True)
async def start_server(interaction: discord.Interaction):
    server_directory = os.getenv("directory")
    global p
    p = subprocess.Popen(server_directory, creationflags=subprocess.CREATE_NEW_CONSOLE, stdin=subprocess.PIPE, text=True)
    await interaction.response.send_message("Server initializing...", ephemeral=True)
@start_server.error
async def start_server_error(ctx, error):
    if isinstance(error, discord.app_commands.MissingPermissions):
        await ctx.response.send_message("You do not have permission to start the server.", ephemeral=True)


@bot.tree.command(name="stop_server", 
                  description="Closes the server using the server command \"stop\"", 
                  guild=Guild
                  )
@discord.app_commands.checks.has_permissions(administrator = True)
async def stop_server(interaction: discord.Interaction):
    global p
    p.communicate(input="stop")
    del p
    await interaction.response.send_message("Server closed", ephemeral=True)
@stop_server.error
async def stop_server_error(ctx, error):
    if isinstance(error, discord.app_commands.MissingPermissions):
        await ctx.response.send_message("You do not have permission to stop the server.", ephemeral=True)


@bot.tree.command(name="command", 
                  description="Passes a string input as a command to the minecraft server",
                  guild=Guild)
@discord.app_commands.checks.has_permissions(administrator = True)
async def command(interaction: discord.Interaction, server_command: str):
    p.stdin.write(server_command + "\n")
    p.stdin.flush()
    #console = p.stdout.read()
    await interaction.response.send_message("Command sent", ephemeral=True)
@command.error
async def command_error(ctx, error):
    if isinstance(error, discord.app_commands.MissingPermissions):
        await ctx.response.send_message(content="You do not have permission to run server commands.", ephemeral=True)


@bot.tree.command(name="mods",
                  description="Requests necessary server mods",
                  guild=Guild)
async def mods(interaction: discord.Interaction):
    user = await interaction.user.create_dm()
    await user.send(r"Install Prominence II using a modpack installer, recommended: https://www.curseforge.com/download/app or https://prismlauncher.org/download")
    await user.send(r"Prominence II: https://www.curseforge.com/minecraft/modpacks/prominence-2-rpg or https://modrinth.com/modpack/prominence-2-fabric")
    await user.send(r"Make sure you install version 2.8.0hf for Fabric 1.20.1!!!") 
    await interaction.response.send_message("Check your DMs :)", ephemeral=True)



bot.run(token)

