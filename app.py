import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# беремо токен з Render Environment
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN не знайдений! Додай його в Render Environment")

# команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Axel Bot працює!")

# команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Напиши /start щоб перевірити бота")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Бот запущений...")

    app.run_polling()

if __name__ == "__main__":
    main()
