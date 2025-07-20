"""
Configuration file for the Telegram bot
"""

import os

# Bot configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Bot settings
MAX_MESSAGE_LENGTH = 4096
SUPPORTED_IMAGE_FORMATS = ['.jpg', '.jpeg', '.png', '.gif', '.webp']

# Trading pairs and exchanges
DEFAULT_TRADING_PAIRS = [
    'BTC/USDT',
    'ETH/USDT', 
    'BNB/USDT',
    'ADA/USDT',
    'SOL/USDT',
    'DOT/USDT',
    'AVAX/USDT',
    'MATIC/USDT'
]

# Time frames for analysis
TIMEFRAMES = ['1h', '4h', '1d', '1w']

# Risk management levels
RISK_LEVELS = {
    'low': {'risk_percent': 1, 'leverage': 1},
    'medium': {'risk_percent': 2, 'leverage': 2},
    'high': {'risk_percent': 3, 'leverage': 3}
}
