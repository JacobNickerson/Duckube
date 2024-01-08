import dotenv
import os


dotenv.load_dotenv()
server_token = os.getenv("server_token")
print(server_token)