from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio

# === Get Bot Token from Environment ===
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Set this in Render environment

# === Create Flask App ===
app = Flask(__name__)

# === Telegram App ===
application = Application.builder().token(BOT_TOKEN).build()

# === Telegram Command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated via Webhook!")

# Add the command handler
application.add_handler(CommandHandler("start", start))

# === Initialize the app ===
asyncio.run(application.initialize())

# === Webhook endpoint ===
@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "", 200

# === Run Flask on port 5000 ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)








