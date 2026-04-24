import asyncio
from datetime import datetime
import pytz

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = "8789015938:AAF-TR7Q-wcerI3juB4jq5tdmw3o7Y7tFVk"


async def nowwhattime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kelowna_tz = pytz.timezone("America/Vancouver")
    singapore_tz = pytz.timezone("Asia/Singapore")

    kelowna_time = datetime.now(kelowna_tz).strftime("%Y-%m-%d %H:%M:%S")
    singapore_time = datetime.now(singapore_tz).strftime("%Y-%m-%d %H:%M:%S")

    message = (
        "🕒 Current Time:\n\n"
        f"🇨🇦 Kelowna: {kelowna_time}\n"
        f"🇸🇬 Singapore: {singapore_time}"
    )

    await update.message.reply_text(message)


async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("nowwhattime", nowwhattime))

    print("Bot is running...")
    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
