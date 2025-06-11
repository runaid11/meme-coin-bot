from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import threading
import asyncio
import os

# ✅ This line reads your token from Render's Environment Variables
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🔔 Webhook received:", data)
    return '', 200

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

async def run_telegram_bot():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

def run_flask():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(run_telegram_bot())



