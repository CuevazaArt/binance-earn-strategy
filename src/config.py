import os
from dotenv import load_dotenv

# Load .env file located at the project root
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise RuntimeError("Binance API credentials not set. Please define BINANCE_API_KEY and BINANCE_API_SECRET in .env")
