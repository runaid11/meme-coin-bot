from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio

# === Load Bot Token from Environment ===
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # set this in Render Environment
WEBHOOK_URL = "https://meme-coin-bot-bhmw.onrender.com/telegram"

# === Flask App ===
app = Flask(__name__)

# === Telegram Bot Setup ===
application = Application.builder().token(BOT_TOKEN).build()

@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "", 200

@app.route("/webhook", methods=["POST"])
def helius_webhook():
    data = request.json
    print("🔔 Helius Webhook received:", data)
    return "", 200

# === Telegram Command Handler ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

application.add_handler(CommandHandler("start", start))

# === Run Everything ===
if __name__ == '__main__':
    # Set Telegram webhook
    async def run():
        await application.bot.set_webhook(WEBHOOK_URL)
        print("✅ Telegram webhook set to:", WEBHOOK_URL)
    asyncio.run(run())

    # Start Flask app
    app.run(host="0.0.0.0", port=5000)




