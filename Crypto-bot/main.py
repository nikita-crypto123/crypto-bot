#!/usr/bin/env python3
"""
Cryptocurrency Trading Signals Telegram Bot
Main entry point for the bot application
"""

import os
import sys
import time
from config import BOT_TOKEN
from bot.handlers import setup_handlers
from utils.logger import setup_logger
import telebot

def main():
    """Main function to start the Telegram bot"""
    logger = setup_logger()
    
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN не найден в переменных окружения")
        sys.exit(1)
    
    try:
        # Initialize bot
        bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')
        
        # Setup handlers
        setup_handlers(bot)
        
        logger.info("Бот запущен и готов к работе...")
        
        # Start polling
        bot.polling(none_stop=True, interval=1, timeout=60)
        
    except Exception as e:
        logger.error(f"Критическая ошибка при запуске бота: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
