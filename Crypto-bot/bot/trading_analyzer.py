"""
Trading analysis and signal generation module
"""

import random
from datetime import datetime
from config import DEFAULT_TRADING_PAIRS, TIMEFRAMES, RISK_LEVELS
from bot.messages import (
    TRADING_IDEA_TEMPLATE, 
    ANALYSIS_RESULT_TEMPLATE,
    PHOTO_ANALYSIS_TEMPLATE
)

class TradingAnalyzer:
    """Class for generating trading ideas and market analysis"""
    
    def __init__(self):
        self.trading_pairs = DEFAULT_TRADING_PAIRS
        self.timeframes = TIMEFRAMES
        self.risk_levels = RISK_LEVELS
    
    def generate_trading_idea(self) -> str:
        """Generate a random trading idea"""
        try:
            # Select random parameters
            pair = random.choice(self.trading_pairs)
            timeframe = random.choice(self.timeframes)
            trade_type = random.choice(['LONG', 'SHORT'])
            risk_level = random.choice(['low', 'medium', 'high'])
            
            # Generate price levels (simplified simulation)
            base_price = random.uniform(0.1, 100000)
            
            if trade_type == 'LONG':
                entry_price = round(base_price, 4)
                tp1 = round(base_price * 1.02, 4)
                tp2 = round(base_price * 1.05, 4)
                tp3 = round(base_price * 1.08, 4)
                stop_loss = round(base_price * 0.97, 4)
            else:
                entry_price = round(base_price, 4)
                tp1 = round(base_price * 0.98, 4)
                tp2 = round(base_price * 0.95, 4)
                tp3 = round(base_price * 0.92, 4)
                stop_loss = round(base_price * 1.03, 4)
            
            # Get risk settings
            risk_settings = self.risk_levels[risk_level]
            
            # Generate reasoning
            reasoning_options = [
                "Техническая формация указывает на продолжение тренда",
                "Пробитие ключевого уровня поддержки/сопротивления",
                "Дивергенция на RSI сигнализирует о развороте",
                "Формация треугольник завершается",
                "Объемы подтверждают движение цены",
                "Уровни Фибоначчи указывают на коррекцию"
            ]
            reasoning = random.choice(reasoning_options)
            
            # Generate idea ID
            idea_id = random.randint(1000, 9999)
            
            # Format the message
            message = TRADING_IDEA_TEMPLATE.format(
                idea_id=idea_id,
                pair=pair,
                timeframe=timeframe,
                trade_type=trade_type,
                entry_price=entry_price,
                tp1=tp1,
                tp2=tp2,
                tp3=tp3,
                stop_loss=stop_loss,
                risk_level=risk_level.upper(),
                leverage=risk_settings['leverage'],
                reasoning=reasoning,
                risk_percent=risk_settings['risk_percent'],
                timestamp=datetime.now().strftime("%d.%m.%Y %H:%M")
            )
            
            return message
            
        except Exception as e:
            return f"❌ Ошибка при генерации торговой идеи: {str(e)}"
    
    def analyze_market(self) -> str:
        """Generate market analysis"""
        try:
            # Generate random market data (in real implementation, this would fetch real data)
            trends = ['Бычий 📈', 'Медвежий 📉', 'Боковой ↔️']
            sentiments = ['Жадность 😈', 'Страх 😱', 'Нейтральное 😐', 'Крайняя жадность 🤑']
            recommendations = ['Покупать', 'Продавать', 'Держать', 'Ждать входа']
            
            trend = random.choice(trends)
            sentiment = random.choice(sentiments)
            recommendation = random.choice(recommendations)
            
            # Generate top cryptos
            top_cryptos = "\n".join([
                f"• {pair}: {random.choice(['📈', '📉'])} {random.uniform(-10, 15):.2f}%"
                for pair in random.sample(self.trading_pairs, 5)
            ])
            
            # Generate key levels
            key_levels_options = [
                "Bitcoin: 42,000$ поддержка, 45,000$ сопротивление",
                "Ethereum: 2,500$ поддержка, 2,800$ сопротивление", 
                "Общий рынок находится в консолидации",
                "Ожидается пробитие треугольника на BTC"
            ]
            key_levels = random.choice(key_levels_options)
            
            # Generate comment
            comments = [
                "Рынок показывает признаки стабилизации после недавней волатильности.",
                "Объемы торгов снижаются, что может указывать на консолидацию.",
                "Макроэкономические факторы оказывают давление на рынок.",
                "Техническая картина остается неопределенной."
            ]
            comment = random.choice(comments)
            
            message = ANALYSIS_RESULT_TEMPLATE.format(
                trend=trend,
                sentiment=sentiment,
                recommendation=recommendation,
                top_cryptos=top_cryptos,
                key_levels=key_levels,
                comment=comment,
                timestamp=datetime.now().strftime("%d.%m.%Y %H:%M")
            )
            
            return message
            
        except Exception as e:
            return f"❌ Ошибка при анализе рынка: {str(e)}"
    
    def analyze_photo(self, photo_info: dict) -> str:
        """Analyze uploaded chart photo"""
        try:
            # In a real implementation, this would use computer vision/AI
            # For now, we'll generate a structured response
            
            patterns_options = [
                "• Восходящий треугольник\n• Пробитие уровня поддержки\n• Дивергенция RSI",
                "• Нисходящий клин\n• Двойная вершина\n• Перепроданность по Stochastic",
                "• Флаг-вымпел\n• Ретест сопротивления\n• Бычья дивергенция MACD",
                "• Голова и плечи\n• Пробитие трендовой линии\n• Объемы подтверждают движение"
            ]
            
            recommendations_options = [
                "• Рассмотреть LONG позицию\n• Дождаться подтверждения пробития\n• Установить тейк-профиты по уровням",
                "• Возможность SHORT позиции\n• Ждать отскока от сопротивления\n• Контролировать риски",
                "• Оставаться в стороне\n• Неопределенная техническая картина\n• Ждать четких сигналов",
                "• Готовиться к развороту\n• Фиксировать прибыль\n• Переносить стопы в безубыток"
            ]
            
            entry_points_options = [
                "• При пробитии: текущая цена + 0.5%\n• При откате: -2% от текущей цены\n• При подтверждении объемом",
                "• На ретесте уровня\n• При закрытии свечи выше сопротивления\n• После формирования пин-бара",
                "• В зоне поддержки\n• При дивергенции индикаторов\n• На пробитии нисходящего тренда"
            ]
            
            risk_management_options = [
                "• Стоп-лосс: 2% от входа\n• Размер позиции: 1-2% депозита\n• Соотношение прибыль/убыток: 1:3",
                "• Трейлинг стоп\n• Частичная фиксация на 50%\n• Максимальный риск: 1% депозита",
                "• Стоп по структуре\n• Пирамидинг при подтверждении\n• Контроль эмоций"
            ]
            
            patterns = random.choice(patterns_options)
            recommendations = random.choice(recommendations_options)
            entry_points = random.choice(entry_points_options)
            risk_management = random.choice(risk_management_options)
            timeframe = random.choice(self.timeframes)
            
            message = PHOTO_ANALYSIS_TEMPLATE.format(
                patterns=patterns,
                recommendations=recommendations,
                entry_points=entry_points,
                risk_management=risk_management,
                timeframe=timeframe,
                timestamp=datetime.now().strftime("%d.%m.%Y %H:%M")
            )
            
            return message
            
        except Exception as e:
            return f"❌ Ошибка при анализе изображения: {str(e)}"
    
    def analyze_text_idea(self, text: str) -> str:
        """Analyze user's trading idea from text"""
        try:
            # Simple text analysis (in real implementation would use NLP)
            text_lower = text.lower()
            
            # Determine sentiment
            bullish_words = ['buy', 'long', 'bull', 'up', 'покупать', 'лонг', 'рост']
            bearish_words = ['sell', 'short', 'bear', 'down', 'продавать', 'шорт', 'падение']
            
            bullish_count = sum(1 for word in bullish_words if word in text_lower)
            bearish_count = sum(1 for word in bearish_words if word in text_lower)
            
            if bullish_count > bearish_count:
                sentiment = "Бычье 📈"
                recommendation = "Рассмотрите LONG позицию"
            elif bearish_count > bullish_count:
                sentiment = "Медвежье 📉"  
                recommendation = "Рассмотрите SHORT позицию"
            else:
                sentiment = "Нейтральное ↔️"
                recommendation = "Дождитесь более четких сигналов"
            
            # Generate analysis points
            analysis_points = [
                f"• Общее настроение: {sentiment}",
                f"• Рекомендация: {recommendation}",
                "• Обязательно используйте стоп-лосс",
                "• Не рискуйте более 2% депозита",
                "• Учитывайте общий тренд рынка"
            ]
            
            analysis = "\n".join(analysis_points)
            
            response = f"""
<b>📝 Анализ вашей идеи</b>

<b>Исходный текст:</b> <i>{text[:200]}{'...' if len(text) > 200 else ''}</i>

<b>🔍 Анализ:</b>
{analysis}

<b>⚠️ Напоминание:</b>
Это предварительная оценка. Всегда проводите собственный анализ и управляйте рисками!

<i>Проанализировано: {datetime.now().strftime("%d.%m.%Y %H:%M")}</i>
"""
            
            return response
            
        except Exception as e:
            return f"❌ Ошибка при анализе текста: {str(e)}"
