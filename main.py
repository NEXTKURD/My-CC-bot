import logging
import requests
import os # ڤێ زێدە بکە
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Token-ێ خۆ ژ Environment Variables بخوینە
TOKEN = os.getenv("TOKEN") 
MY_CHAT_ID = "7013641187"

async def process_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_chat.id) != MY_CHAT_ID:
        return

    user_text = update.message.text
    await update.message.reply_text("بوهێلە، ئەز یێ ب ڕێیا سێرڤەری دچمه سەر سایتێ...")

    try:
        url = "https://uncoder.eu.org/cc-checker/check"
        data = {'card': user_text}
        
        # ل ڤێرێ بکارئینانا 'timeout' گەلەک یا گرنگە داکو سێرڤەر نەراوەستیت
        response = requests.post(url, data=data, timeout=10)
        
        result = "ئەنجام: " + response.text
        await update.message.reply_text(result)
        
    except Exception as e:
        await update.message.reply_text(f"ئاریشەیەک هات: {str(e)}")

if __name__ == '__main__':
    # گوهۆڕینا کێم ل سەر کارپێکرنێ
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), process_data))
    app.run_polling()
