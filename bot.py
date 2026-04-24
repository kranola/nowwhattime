import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import pytz

TOKEN = "8789015938:AAF-TR7Q-wcerI3juB4jq5tdmw3o7Y7tFVk"

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kelowna_tz = pytz.timezone("America/Vancouver")
    singapore_tz = pytz.timezone("Asia/Singapore")

    kelowna_time = datetime.now(kelowna_tz).strftime("%Y-%m-%d %H:%M:%S")
    singapore_time = datetime.now(singapore_tz).strftime("%Y-%m-%d %H:%M:%S")

    message = (
        f"🇨🇦 Kelowna: {kelowna_time}\n"
        f"🇸🇬 Singapore: {singapore_time}"
    )

    await update.message.reply_text(message)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("nowwhatime", time_command))

    print("Bot is running...")
    app.run_polling()
