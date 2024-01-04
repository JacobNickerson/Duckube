import os
import dotenv

dotenv.load_dotenv()
token = os.getenv('discord_token')
print(token)