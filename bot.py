from datetime import datetime
from zoneinfo import ZoneInfo

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8789015938:AAF-TR7Q-wcerI3juB4jq5tdmw3o7Y7tFVk"


async def nowwhattime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kelowna_time = datetime.now(ZoneInfo("America/Vancouver")).strftime("%Y-%m-%d %H:%M:%S")
    singapore_time = datetime.now(ZoneInfo("Asia/Singapore")).strftime("%Y-%m-%d %H:%M:%S")

    message = (
        "🕒 Current Time:\n\n"
        f"🇨🇦 Kelowna: {kelowna_time}\n"
        f"🇸🇬 Singapore: {singapore_time}"
    )

    await update.message.reply_text(message)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("nowwhattime", nowwhattime))

    print("Bot is running...")
    app.run_polling()   # ✅ IMPORTANT: no await, no asyncio


if __name__ == "__main__":
    main()
