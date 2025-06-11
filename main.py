from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import threading
import asyncio
import os

# === Telegram Bot ===
BOT_TOKEN = os.getenv('7920309268:AAELcWXpPST_Anjr9gH4aorT1_fklKEJnl8')  # Set this in Render environment variables

app = Flask(__name__)

# === Flask Webhook Route ===
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🔔 Webhook received:", data)
    # You can enhance this to filter wallet, txs, etc.
    return '', 200

# === Telegram Bot Handlers ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

# === Run Telegram Bot ===
async def run_telegram_bot():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

# === Run Flask App on Port 5000 ===
def run_flask():
    app.run(host="0.0.0.0", port=5000)

# === Start Both (Flask + Telegram) ===
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(run_telegram_bot())


