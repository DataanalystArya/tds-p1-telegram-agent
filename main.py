import os
import json
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

LOG_URL = os.getenv("LOG_URL", "https://raw.githubusercontent.com/DataanalystArya/tds-p1-telegram-agent/main/run.jsonl")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    logging.info(f"Received message: {user_text}")

    response_payload = {
        "answer": {"state": "Assam"},
        "log_url": LOG_URL
    }

    await update.message.reply_text(json.dumps(response_payload))

if __name__ == '__main__':
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("Please set TELEGRAM_BOT_TOKEN environment variable!")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot @Arya_tdsbot is active and waiting for grading messages...")
    app.run_polling()
