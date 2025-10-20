import os
from dotenv import load_dotenv
from bot import Bot

load_dotenv()

bot = Bot(prefix='!')

token = os.getenv("DISCORD_BOT_TOKEN")
if token is None:
    raise ValueError("DISCORD_BOT_TOKEN is not set in the environment variables.")

bot.run(token=token)