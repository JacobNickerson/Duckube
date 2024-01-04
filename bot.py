import discord
from dotenv import load_dotenv
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
    

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
token = os.getenv('discord_token')
client = MyClient(intents=intents)
client.run(token)


server_token = os.getenv('guild_token')
@MyClient.event
async def on_ready():
    for guild in MyClient.guilds:
        if guild.name == server_token:
            break
