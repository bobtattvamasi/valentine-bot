# Архитектура

## Схема
[Девушка в Telegram]
↓ /start
[Telegram Bot (Python)]
↓ отправляет кнопку WebApp
[Telegram Web App]
↓ открывается внутри Telegram
[valentine webapp на Vercel]
↓ красивая валентинка с анимациями
↓ кнопка “Перейти на сайт”
[Основной сайт девушки]

## Компоненты

### 1. Telegram Bot (`bot/main.py`)
- Фреймворк: python-telegram-bot v20+
- Единственная команда: /start
- Отправляет InlineKeyboard с WebApp кнопкой

### 2. Web App (`webapp/`)
- Чистый HTML/CSS/JS
- Подключен Telegram Web App SDK
- Многошаговая валентинка с анимациями
- Финальная кнопка → ссылка на сайт
- Деплой: Vercel