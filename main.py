from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import asyncio

# ✅ Read token from environment
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ✅ Flask setup
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🔔 Webhook received:", data)
    return '', 200

# ✅ Telegram handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

# ✅ Main entry point for both Flask + Bot
async def main():
    # Start Flask server in background
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, lambda: app.run(host="0.0.0.0", port=5000))

    # Start Telegram bot
    app_telegram = ApplicationBuilder().token(BOT_TOKEN).build()
    app_telegram.add_handler(CommandHandler("start", start))
    print("✅ Telegram bot is starting...")
    await app_telegram.run_polling()

if __name__ == "__main__":
    asyncio.run(main())







