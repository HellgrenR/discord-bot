import os
from dotenv import load_dotenv
from bot import Bot

load_dotenv()

bot = Bot(prefix='!')

bot.run(token=os.getenv("DISCORD_BOT_TOKEN"))