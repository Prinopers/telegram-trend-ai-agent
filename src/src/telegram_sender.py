from src.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from telegram import Bot

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send_message(message):
    bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=message
    )

if __name__ == "__main__":
    send_message("Telegram Trend AI Agent is running.")
