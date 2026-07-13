import logging
import requests
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# خویندنا Token ژ سێرڤەری
TOKEN = os.getenv("TOKEN") 

# ڤێ پەیاما خێرهاتنێ زێدە کر
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("بخيرهاتى بو NEXT CHECK")

async def process_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    print(f"پەیامەک هات: {user_text}") 
    
    await update.message.reply_text("بوهێلە، ئەز یێ ب ڕێیا سێرڤەری دچمه سەر سایتێ...")

    try:
        url = "https://uncoder.eu.org/cc-checker/check"
        data = {'card': user_text}
        response = requests.post(url, data=data, timeout=10)
        result = "ئەنجام: " + response.text
        await update.message.reply_text(result)
    except Exception as e:
        await update.message.reply_text(f"ئاریشەیەک هات: {str(e)}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    # گرێدانا فەرمانا ستارت
    app.add_handler(CommandHandler("start", start))
    # گرێدانا پەیامێن ئاسایی
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), process_data))
    
    print("بۆت دەست ب کار بوو و یێ چاڤەڕێی پەیامانە...")
    app.run_polling()
