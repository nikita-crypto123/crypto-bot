"""
Bot messages and text constants in Russian
"""

# Welcome and help messages
WELCOME_MESSAGE = """
🤖 <b>Добро пожаловать в CryptoSignals Bot!</b>

Я помогу вам с анализом криптовалютных сделок и предоставлю торговые сигналы.

<b>Доступные команды:</b>
/start - Запуск бота
/help - Показать помощь
/idea - Получить торговую идею
/analyze - Анализ рынка

Вы также можете отправить мне:
📷 Скриншот графика для анализа
📝 Описание сделки для проверки

Удачных торгов! 📈
"""

HELP_MESSAGE = """
<b>📋 Справка по командам:</b>

<b>/start</b> - Запустить бота заново
<b>/help</b> - Показать это сообщение
<b>/idea</b> - Получить случайную торговую идею
<b>/analyze</b> - Получить анализ текущего рынка

<b>🖼️ Анализ скриншотов:</b>
Отправьте скриншот торгового графика, и я дам рекомендации по входу/выходу.

<b>📝 Анализ текста:</b>
Опишите вашу торговую идею текстом, и я оценю её потенциал.

<b>⚠️ Предупреждение:</b>
Все сигналы носят рекомендательный характер. Торгуйте на свой страх и риск!
"""

# Trading idea templates
TRADING_IDEA_TEMPLATE = """
<b>💡 Торговая идея #{idea_id}</b>

<b>🪙 Пара:</b> {pair}
<b>⏰ Таймфрейм:</b> {timeframe}
<b>📊 Тип сделки:</b> {trade_type}

<b>📈 Вход:</b> {entry_price}
<b>🎯 Цели:</b>
• TP1: {tp1}
• TP2: {tp2}
• TP3: {tp3}

<b>🛡️ Стоп-лосс:</b> {stop_loss}
<b>⚖️ Риск:</b> {risk_level}
<b>🔢 Плечо:</b> {leverage}x

<b>📝 Обоснование:</b>
{reasoning}

<b>⚠️ Риск-менеджмент:</b>
Не рискуйте более {risk_percent}% от депозита на одну сделку!

<i>Время создания: {timestamp}</i>
"""

ANALYSIS_RESULT_TEMPLATE = """
<b>🔍 Анализ рынка</b>

<b>📊 Общий тренд:</b> {trend}
<b>📈 Настроение рынка:</b> {sentiment}
<b>🎯 Рекомендация:</b> {recommendation}

<b>📋 Топ криптовалют сейчас:</b>
{top_cryptos}

<b>⚠️ Важные уровни:</b>
{key_levels}

<b>💭 Комментарий:</b>
{comment}

<i>Обновлено: {timestamp}</i>
"""

PHOTO_ANALYSIS_TEMPLATE = """
<b>🖼️ Анализ графика</b>

<b>📊 Обнаруженные паттерны:</b>
{patterns}

<b>🎯 Рекомендации:</b>
{recommendations}

<b>📈 Точки входа:</b>
{entry_points}

<b>🛡️ Управление рисками:</b>
{risk_management}

<b>⏰ Таймфрейм:</b> {timeframe}

<i>Анализ выполнен: {timestamp}</i>
"""

# Error messages
ERROR_GENERAL = "❌ Произошла ошибка. Попробуйте позже."
ERROR_INVALID_COMMAND = "❌ Неизвестная команда. Используйте /help для просмотра доступных команд."
ERROR_PROCESSING_IMAGE = "❌ Ошибка при обработке изображения. Попробуйте отправить другое изображение."
ERROR_INVALID_FORMAT = "❌ Неподдерживаемый формат файла. Поддерживаются: JPG, PNG, GIF, WebP."

# Success messages
SUCCESS_ANALYSIS_STARTED = "✅ Начинаю анализ..."
SUCCESS_IDEA_GENERATED = "✅ Торговая идея сгенерирована!"
SUCCESS_MARKET_ANALYZED = "✅ Анализ рынка завершен!"
