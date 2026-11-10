import os

from dotenv import load_dotenv

# Read the .env files into environment variables
load_dotenv()

# Discord variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID") or 0) # 0 until I get the real ID

# GPT variables
# Blank OpenAI key until I add one
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# RSS feeds
FEED_URLS = [u.strip() for u in os.getenv("FEED_URLS", "").split(",") if u.strip()]

# Interval of checking news links (in minutes)
CHECK_INTERVAL_MINUTES = int(os.getenv("CHECK_INTERVAL_MINUTES") or 30)

