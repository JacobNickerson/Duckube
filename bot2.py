import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


class DuckBot(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} is quacking!')
    

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author.id == self.user.id:
            return


load_dotenv()
token = os.getenv("discord_token")
intents = discord.Intents.default()
intents.message_content = True
bot = DuckBot(command_prefix="/", intents=intents)
bot.run(token)