from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio
import os

# === Load Telegram Token from Render Environment ===
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# === Flask App ===
app = Flask(__name__)

# === Telegram Bot Setup ===
application = Application.builder().token(BOT_TOKEN).build()

@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "", 200

# === Telegram Command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

application.add_handler(CommandHandler("start", start))

# === Start Flask ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)







