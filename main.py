from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio
import os

# === Load Bot Token from Environment ===
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# === Flask App ===
app = Flask(__name__)

# === Telegram Bot Setup ===
application = Application.builder().token(BOT_TOKEN).concurrent_updates(True).build()

# === /start command handler ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

application.add_handler(CommandHandler("start", start))

# === Telegram Webhook Route ===
@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "", 200

# === Main Entrypoint for Render ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)









