import logging
import os
from typing import Final

from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

logging.basicConfig(
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN: Final[str | None] = os.getenv("BOT_TOKEN")
WEBAPP_URL: Final[str | None] = os.getenv("WEBAPP_URL")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if WEBAPP_URL is None:
        logger.error("WEBAPP_URL is not set")
        await update.message.reply_text("Ошибка конфигурации: WEBAPP_URL не задан.")
        return

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Открой валентинку 💝",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ]
    )

    await update.message.reply_text(
        "💕 Привет, моя любимая! У меня есть для тебя сюрприз...",
        reply_markup=keyboard,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Этот бот отправляет валентинку в формате Telegram Web App.\n"
        "Команды:\n"
        "/start — открыть валентинку\n"
        "/help — показать это сообщение"
    )


def main() -> None:
    if BOT_TOKEN is None:
        raise RuntimeError("BOT_TOKEN is not set in environment")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    logger.info("Bot is running")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
