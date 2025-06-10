from flask import Flask, request
from telegram.ext import Application, CommandHandler
import asyncio
import threading
import nest_asyncio
nest_asyncio.apply()


# ✅ Your bot token
TOKEN = '7920309268:AAELcWXpPST_Anjr9gH4aorT1_fklKEJnl8'

# ✅ Flask app
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 New Transaction Alert:", data)
    return {'status': 'received'}

# ✅ Telegram command handler
async def start(update, context):
    await update.message.reply_text("✅ Meme Coin AI Bot Activated!")

# ✅ Telegram bot runner
async def run_telegram_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running...")
    await application.run_polling()

# ✅ Main event loop
async def main():
    # Start the Telegram bot
    telegram_task = asyncio.create_task(run_telegram_bot())

    # Start the Flask app in a thread
    def run_flask():
        app.run(host='0.0.0.0', port=5000)

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    await telegram_task

if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
