import asyncio
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from flask import Flask 

TOKEN = 'YOUR_TELEGRAM_BOT_API' #ENTER YOUR TELEGRAM BOT API
CHANNEL_ID = '@your_channel_id'  # ENTER YOUR CHANNEL ID

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

async def check_time_loop():
    while True:
        now = asyncio.get_event_loop().run_in_executor(None, lambda: telegram.utils.helpers.now())
        now = await now
        hours = now.hour
        minutes = now.minute

        if hours == minutes:
            try:
                await bot.send_message(chat_id=CHANNEL_ID, text=f'{hours}:{minutes}')
                print(f"Message sent: {hours}:{minutes}")
            except Exception as e:
                print(f"Error in sending message: {e}")
        await asyncio.sleep(50)  

def handle_message(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Do not text me!")

@app.route('/')
def home():
    return 'Telegram bot is activated'

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()

    loop = asyncio.get_event_loop()
    loop.create_task(check_time_loop())

    app.run(port=3000)

if __name__ == '__main__':
    main()