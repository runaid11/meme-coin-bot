from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import os

# ✅ Get token from Render environment variable
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# === Flask app
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("🔔 Webhook received:", data)
    return "", 200

# === Telegram /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

# === Async main runner
async def main():
    # 1. Run Flask in background
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, lambda: app.run(host="0.0.0.0", port=5000))

    # 2. Run Telegram bot
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    await app_bot.initialize()
    await app_bot.start()
    await app_bot.updater.start_polling()
    await app_bot.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())








