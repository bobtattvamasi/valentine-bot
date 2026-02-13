# Valentine Bot

Telegram-бот с Web App валентинкой: бот отправляет кнопку, а внутри Telegram открывается многошаговая страница с анимациями и ссылкой на сайт.

## Запуск бота

```bash
cd bot
pip install -r requirements.txt
python main.py
```

Перед запуском создайте `bot/.env` на основе `bot/.env.example`.

## Деплой webapp

```bash
cd webapp
vercel --prod
```
