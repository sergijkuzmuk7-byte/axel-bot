import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import threading

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN не знайдений!")

# Telegram bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Бот працює!")

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущений...")
    app.run_polling()

# Flask (щоб Render був задоволений)
web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    # запускаємо бота в окремому потоці
    threading.Thread(target=run_bot).start()

    # запускаємо веб сервер
    web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
