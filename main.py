from flask import Flask, request
from telegram.ext import Application, CommandHandler
import nest_asyncio
import asyncio
import threading

# ✅ Your bot token
TOKEN = '7920309268:AAELcWXpPST_Anjr9gH4aorT1_fklKEJnl8'

# ✅ Flask app
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🚨 New Transaction Alert:", data)
    return {'status': 'received'}

# ✅ Telegram command handler
async def start(update, context):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

# ✅ Telegram bot runner
async def run_telegram_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

# ✅ Threaded bot runner
def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    nest_asyncio.apply()  # Fix for RuntimeError
    loop.run_until_complete(run_telegram_bot())

# ✅ Start thread
threading.Thread(target=start_bot).start()



