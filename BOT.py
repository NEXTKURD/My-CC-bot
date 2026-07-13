import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ئاگەهدارکرنا لۆگێن بۆتی
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "8869335780:AAEKJGZg4LJnKw_pC-f3vBFShfKhe8VwCug"
MY_CHAT_ID = "7013641187"

async def process_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_chat.id) != MY_CHAT_ID:
        return

    user_text = update.message.text
    await update.message.reply_text("بوهێلە، ئەز یێ ب ڕێیا سێرڤەری دچمه سەر سایتێ...")

    try:
        # کارکرن ل سەر سایتێ ب ڕێیا API (ئەڤە بێی برۆسەرە و زووترە)
        # ل ڤێرێ پێدڤییە تو URL-یا ڕاستەقینە یا POST-ا سایتێ بزانی
        url = "https://uncoder.eu.org/cc-checker/check" # نموونە
        data = {'card': user_text}
        
        response = requests.post(url, data=data)
        
        result = "ئەنجام: " + response.text
        await update.message.reply_text(result)
        
    except Exception as e:
        await update.message.reply_text(f"ئاریشەیەک هات: {str(e)}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), process_data))
    app.run_polling()
