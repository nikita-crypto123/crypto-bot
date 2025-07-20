# Cryptocurrency Trading Signals Telegram Bot

## Overview

This is a Telegram bot designed to provide cryptocurrency trading signals and market analysis. The bot can analyze trading charts from screenshots, generate random trading ideas, and provide market insights. It's built using Python with the `telebot` library and follows a modular architecture for easy maintenance and extensibility.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Application Type
**Telegram Bot Application** - A standalone Python application that interfaces with Telegram's Bot API to provide cryptocurrency trading analysis and signals.

### Architecture Pattern
**Modular Monolith** - The application is structured as a single deployable unit with clear separation of concerns across different modules:
- `bot/` - Core bot functionality (handlers, messages, trading analysis)
- `utils/` - Shared utilities (logging)
- `config.py` - Centralized configuration
- `main.py` - Application entry point

## Key Components

### 1. Bot Core (`main.py`)
- **Purpose**: Application entry point and bot initialization
- **Responsibilities**: Environment validation, bot setup, error handling, and polling management
- **Technology**: Uses `telebot` library for Telegram Bot API integration

### 2. Message Handlers (`bot/handlers.py`)
- **Purpose**: Process incoming Telegram messages and commands
- **Supported Commands**:
  - `/start` - Bot initialization and welcome
  - `/help` - Command documentation
  - `/idea` - Generate trading recommendations
  - `/analyze` - Market analysis
- **Image Processing**: Handles screenshot analysis for trading charts
- **Technology**: Event-driven handlers using telebot decorators

### 3. Trading Analysis Engine (`bot/trading_analyzer.py`)
- **Purpose**: Core business logic for generating trading signals
- **Features**:
  - Random trading idea generation
  - Price level calculations (entry, take-profit, stop-loss)
  - Risk management integration
  - Support for LONG/SHORT positions
- **Data Sources**: Uses predefined trading pairs and timeframes from configuration

### 4. Message Templates (`bot/messages.py`)
- **Purpose**: Centralized text content management
- **Language**: Russian language support
- **Content Types**: Welcome messages, help text, trading templates, error messages

### 5. Configuration Management (`config.py`)
- **Purpose**: Centralized application settings
- **Key Settings**:
  - Bot token management
  - Trading pairs (BTC/USDT, ETH/USDT, etc.)
  - Risk levels with leverage settings
  - Supported image formats
  - Message length limits

### 6. Logging System (`utils/logger.py`)
- **Purpose**: Application monitoring and debugging
- **Features**: Console logging with structured formatting
- **Level**: INFO level logging for operational visibility

## Data Flow

### Command Processing Flow
1. User sends command/message to Telegram
2. Telegram forwards to bot via webhooks/polling
3. `handlers.py` routes message to appropriate handler
4. Handler processes request using `TradingAnalyzer` if needed
5. Response formatted using templates from `messages.py`
6. Bot sends response back to user via Telegram API

### Trading Idea Generation Flow
1. User requests trading idea (`/idea` command)
2. `TradingAnalyzer.generate_trading_idea()` called
3. Random selection of trading pair, timeframe, and direction
4. Price calculations based on simulated market data
5. Risk management parameters applied
6. Formatted response sent to user

## External Dependencies

### Required Libraries
- `telebot` - Telegram Bot API wrapper
- `os` - Environment variable access
- `random` - Trading idea randomization
- `datetime` - Timestamp handling
- `logging` - Application logging

### Telegram Bot API
- **Purpose**: Core communication interface
- **Authentication**: Bot token from environment variables
- **Features Used**: Message sending, command handling, image processing

## Deployment Strategy

### Environment Setup
- **Bot Token**: Required environment variable `BOT_TOKEN`
- **Error Handling**: Application exits if token not provided
- **Logging**: Console output for monitoring

### Runtime Configuration
- **Polling Mode**: Continuous polling with 1-second intervals
- **Timeout**: 60-second timeout for API calls
- **Error Recovery**: Automatic restart on critical errors
- **Parse Mode**: HTML formatting for rich text messages

### Scalability Considerations
- **Current State**: Single-instance deployment
- **Bottlenecks**: Synchronous message processing
- **Future Enhancements**: Could benefit from async processing for high-volume scenarios

## Architecture Decisions

### Why Telegram Bot Framework
- **Problem**: Need for accessible cryptocurrency analysis tool
- **Solution**: Telegram bot provides instant access without app installation
- **Benefits**: Cross-platform, real-time notifications, easy user interaction

### Why Modular Structure
- **Problem**: Maintainability and code organization
- **Solution**: Clear separation between bot logic, analysis, and configuration
- **Benefits**: Easy testing, feature additions, and bug isolation

### Why Simulated Trading Data
- **Problem**: Complexity of real-time market data integration
- **Solution**: Randomized but realistic trading scenarios
- **Benefits**: Simplified development, consistent demo functionality
- **Trade-offs**: Not suitable for real trading decisions

### Why Russian Language Interface
- **Problem**: Target audience language preference
- **Solution**: All user-facing text in Russian
- **Benefits**: Better user experience for Russian-speaking traders