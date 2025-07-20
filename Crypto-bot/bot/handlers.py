"""
Telegram bot message handlers
"""

import telebot
from telebot import types
from utils.logger import setup_logger
from bot.messages import (
    WELCOME_MESSAGE, 
    HELP_MESSAGE,
    ERROR_GENERAL,
    ERROR_INVALID_COMMAND,
    ERROR_PROCESSING_IMAGE,
    ERROR_INVALID_FORMAT,
    SUCCESS_ANALYSIS_STARTED,
    SUCCESS_IDEA_GENERATED,
    SUCCESS_MARKET_ANALYZED
)
from bot.trading_analyzer import TradingAnalyzer
from config import SUPPORTED_IMAGE_FORMATS

# Initialize logger and analyzer
logger = setup_logger()
analyzer = TradingAnalyzer()

def setup_handlers(bot: telebot.TeleBot):
    """Setup all bot message handlers"""
    
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        """Handle /start command"""
        try:
            logger.info(f"User {message.from_user.id} started the bot")
            
            # Send welcome message
            bot.send_message(
                message.chat.id,
                WELCOME_MESSAGE,
                parse_mode='HTML'
            )
            
        except Exception as e:
            logger.error(f"Error handling /start: {e}")
            bot.send_message(message.chat.id, ERROR_GENERAL)
    
    @bot.message_handler(commands=['help'])
    def handle_help(message):
        """Handle /help command"""
        try:
            logger.info(f"User {message.from_user.id} requested help")
            
            bot.send_message(
                message.chat.id,
                HELP_MESSAGE,
                parse_mode='HTML'
            )
            
        except Exception as e:
            logger.error(f"Error handling /help: {e}")
            bot.send_message(message.chat.id, ERROR_GENERAL)
    
    @bot.message_handler(commands=['idea'])
    def handle_idea(message):
        """Handle /idea command - generate trading idea"""
        try:
            logger.info(f"User {message.from_user.id} requested trading idea")
            
            # Send processing message
            processing_msg = bot.send_message(message.chat.id, SUCCESS_ANALYSIS_STARTED)
            
            # Generate trading idea
            trading_idea = analyzer.generate_trading_idea()
            
            # Delete processing message and send result
            bot.delete_message(message.chat.id, processing_msg.message_id)
            bot.send_message(
                message.chat.id,
                trading_idea,
                parse_mode='HTML'
            )
            
            logger.info(f"Trading idea sent to user {message.from_user.id}")
            
        except Exception as e:
            logger.error(f"Error handling /idea: {e}")
            bot.send_message(message.chat.id, ERROR_GENERAL)
    
    @bot.message_handler(commands=['analyze'])
    def handle_analyze(message):
        """Handle /analyze command - market analysis"""
        try:
            logger.info(f"User {message.from_user.id} requested market analysis")
            
            # Send processing message
            processing_msg = bot.send_message(message.chat.id, SUCCESS_ANALYSIS_STARTED)
            
            # Generate market analysis
            market_analysis = analyzer.analyze_market()
            
            # Delete processing message and send result
            bot.delete_message(message.chat.id, processing_msg.message_id)
            bot.send_message(
                message.chat.id,
                market_analysis,
                parse_mode='HTML'
            )
            
            logger.info(f"Market analysis sent to user {message.from_user.id}")
            
        except Exception as e:
            logger.error(f"Error handling /analyze: {e}")
            bot.send_message(message.chat.id, ERROR_GENERAL)
    
    @bot.message_handler(content_types=['photo'])
    def handle_photo(message):
        """Handle photo uploads for chart analysis"""
        try:
            logger.info(f"User {message.from_user.id} sent a photo for analysis")
            
            # Send processing message
            processing_msg = bot.send_message(message.chat.id, SUCCESS_ANALYSIS_STARTED)
            
            # Get photo info
            photo = message.photo[-1]  # Get the highest resolution photo
            photo_info = {
                'file_id': photo.file_id,
                'width': photo.width,
                'height': photo.height,
                'file_size': photo.file_size
            }
            
            # Analyze photo
            analysis_result = analyzer.analyze_photo(photo_info)
            
            # Delete processing message and send result
            bot.delete_message(message.chat.id, processing_msg.message_id)
            bot.send_message(
                message.chat.id,
                analysis_result,
                parse_mode='HTML'
            )
            
            logger.info(f"Photo analysis sent to user {message.from_user.id}")
            
        except Exception as e:
            logger.error(f"Error handling photo: {e}")
            bot.send_message(message.chat.id, ERROR_PROCESSING_IMAGE)
    
    @bot.message_handler(content_types=['document'])
    def handle_document(message):
        """Handle document uploads"""
        try:
            logger.info(f"User {message.from_user.id} sent a document")
            
            # Check if it's an image file
            if message.document.mime_type and message.document.mime_type.startswith('image/'):
                # Treat as image
                processing_msg = bot.send_message(message.chat.id, SUCCESS_ANALYSIS_STARTED)
                
                photo_info = {
                    'file_id': message.document.file_id,
                    'file_name': message.document.file_name,
                    'mime_type': message.document.mime_type,
                    'file_size': message.document.file_size
                }
                
                analysis_result = analyzer.analyze_photo(photo_info)
                
                bot.delete_message(message.chat.id, processing_msg.message_id)
                bot.send_message(
                    message.chat.id,
                    analysis_result,
                    parse_mode='HTML'
                )
            else:
                bot.send_message(
                    message.chat.id,
                    "❌ Поддерживаются только изображения. Отправьте скриншот торгового графика."
                )
                
        except Exception as e:
            logger.error(f"Error handling document: {e}")
            bot.send_message(message.chat.id, ERROR_PROCESSING_IMAGE)
    
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        """Handle text messages - analyze trading ideas"""
        try:
            # Skip if it's a command we don't recognize
            if message.text.startswith('/'):
                bot.send_message(message.chat.id, ERROR_INVALID_COMMAND)
                return
            
            logger.info(f"User {message.from_user.id} sent text for analysis: {message.text[:50]}...")
            
            # Send processing message
            processing_msg = bot.send_message(message.chat.id, SUCCESS_ANALYSIS_STARTED)
            
            # Analyze the text
            analysis_result = analyzer.analyze_text_idea(message.text)
            
            # Delete processing message and send result
            bot.delete_message(message.chat.id, processing_msg.message_id)
            bot.send_message(
                message.chat.id,
                analysis_result,
                parse_mode='HTML'
            )
            
            logger.info(f"Text analysis sent to user {message.from_user.id}")
            
        except Exception as e:
            logger.error(f"Error handling text: {e}")
            bot.send_message(message.chat.id, ERROR_GENERAL)
    
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(call):
        """Handle inline keyboard callbacks"""
        try:
            logger.info(f"User {call.from_user.id} pressed callback: {call.data}")
            
            # Answer callback to remove loading state
            bot.answer_callback_query(call.id)
            
            # Handle different callback data
            if call.data == 'new_idea':
                # Generate new trading idea
                trading_idea = analyzer.generate_trading_idea()
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text=trading_idea,
                    parse_mode='HTML'
                )
            
        except Exception as e:
            logger.error(f"Error handling callback: {e}")
            bot.answer_callback_query(call.id, "❌ Произошла ошибка")
    
    # Note: Middleware functionality moved to individual handlers for better compatibility
