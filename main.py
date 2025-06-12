from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio

# === Load Bot Token ===
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Set this in Render
app = Flask(__name__)
application = Application.builder().token(BOT_TOKEN).build()

# === Telegram Command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

application.add_handler(CommandHandler("start", start))

# === Telegram Webhook Endpoint ===
@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "", 200

# === Start Server ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)






