import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print("STARTING...")

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    print("❌ TOKEN IS NONE")
    exit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Бот працює!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ BOT STARTED")

app.run_polling()
