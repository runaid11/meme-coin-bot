from flask import Flask, request
from telegram.ext import Application, CommandHandler
import asyncio
import threading
import nest_asyncio

# ✅ Your bot token (replace with your real one)
TOKEN = '7920309268:AAELcWXpPST_Anjr9gH4aorT1_fklKEJnl8'

# ✅ Flask app for Helius webhook
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🚨 New Transaction Alert:", data)
    return {'status': 'received'}

# ✅ Telegram /start command
async def start(update, context):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

# ✅ Start Telegram bot
async def run_telegram_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

# ✅ Patch event loop issues (for Render + Flask combo)
nest_asyncio.apply()

# ✅ Run Flask + Telegram bot together
def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    # Start Flask in a thread
    threading.Thread(target=run_flask).start()
    # Run the Telegram bot
    asyncio.run(run_telegram_bot())


