from flask import Flask, request
from telegram.ext import Application, CommandHandler
import threading
import asyncio

# ✅ Telegram Bot Token
TOKEN = '7920309268:AAELcWXpPST_Anjr9gH4aorT1_fklKEJnl8'

# ✅ Flask App
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🔔 New Transaction Alert:", data)
    return {'status': 'received'}

# ✅ Telegram Command Handler
async def start(update, context):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

# ✅ Run Telegram Bot in Background Thread
async def run_telegram_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

def start_bot_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_telegram_bot())

# ✅ Start both Flask + Telegram
if __name__ == '__main__':
    bot_thread = threading.Thread(target=start_bot_thread)
    bot_thread.start()
    app.run(host='0.0.0.0', port=5000)

