# Changelog

## v1.2.1 — Pre-release Cleanup
- Обновлены docs/TASKS.md и docs/CONTENT.md
- Добавлен .idea/ в .gitignore
- Удалён bot/.env из отслеживания git

## v1.2.0 — Webhook Migration For Vercel
- Добавлен serverless entrypoint `api/webhook.py` для Telegram webhook (без `python-telegram-bot`)
- Обработка `/start` перенесена на прямой вызов Telegram Bot API `sendMessage`
- Конфигурация перенесена в корневой `vercel.json` (rewrites для API и `webapp/*`)
- Добавлен корневой `requirements.txt` с `httpx==0.27.0` для Python function на Vercel
- Удалён `webapp/vercel.json` как устаревший после переноса конфига в корень

## v1.1.0 — MVP Scaffold Refresh
- Добавлен `bot/main.py` на `python-telegram-bot==20.7` с командами `/start` и `/help`
- Подключены `.env` переменные (`BOT_TOKEN`, `WEBAPP_URL`) через `python-dotenv`
- Добавлены `bot/requirements.txt` и `bot/.env.example`
- Реализована Web App валентинка (3 шага) в `webapp/index.html`
- Добавлены стили и анимации в `webapp/style.css` (glassmorphism, pulse, fadeInUp, floatUp, confettiFall)
- Добавлена логика Telegram Web App, пошаговые переходы, фоновые сердечки и конфетти в `webapp/script.js`
- Добавлен `webapp/vercel.json` с rewrite всех путей на `index.html`
- Добавлены `.gitignore` и `README.md` с инструкциями запуска и деплоя
- Обновлён `docs/TASKS.md`: выполненные пункты отмечены

## v1.0.0 — Valentine's Day Edition 💝
- Создан Telegram бот
- Создана Web App валентинка
- 3 шага: приветствие → признание → ссылка на сайт
- Анимации: летающие сердечки, пульсация, fadeIn
- Деплой webapp на Vercel
