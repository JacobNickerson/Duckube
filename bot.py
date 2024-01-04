import discord
from dotenv import load_dotenv
import os

class DuckBot(discord.Client):
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=server_token))
        channel = self.get_channel(server_token)
        print(f'{self.user} is quacking!')
    

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('!help'):
            await message.channel.send("Check your DMs :duck:")


class MyTree(discord.app_commands.CommandTree):
    def add_commands(self):
        @self.command(name="testcommand", 
            description="a fake command for testing")
        
        async def first_command(interaction):
            await interaction.response.send_message("WOAH!!!")
        
load_dotenv()
token = os.getenv("discord_token")
server_token = os.getenv("server_token")

intents = discord.Intents.default()
intents.message_content = True
bot = DuckBot(intents=intents)
tree = MyTree


bot.run(token)
