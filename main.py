from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import os

# ✅ Reads bot token from environment variable
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("🔔 Webhook received:", data)
    return "", 200

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

async def main():
    # Start Flask server in background
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, lambda: app.run(host="0.0.0.0", port=5000))

    # Start Telegram bot
    bot_app = ApplicationBuilder().token(BOT_TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    await bot_app.initialize()
    await bot_app.start()
    print("✅ Telegram bot is live and polling...")
    await bot_app.updater.start_polling()
    await bot_app.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())


