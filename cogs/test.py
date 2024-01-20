import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()
server_token = os.getenv("discord_server_token")

class Test(commands.Cog, name="test_commands"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @discord.slash_command(name="test_command", description="a command for testing the moving of commands to cogs")
    async def test_command(self, ctx):
        await ctx.response.send_message("Success!", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Test(bot))
