from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import pytz

# Replace this with your bot token
BOT_TOKEN = "8789015938:AAF-TR7Q-wcerI3juB4jq5tdmw3o7Y7tFVk"

# Function for /nowwhattime command
async def nowwhattime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Timezones
    kelowna_tz = pytz.timezone("America/Vancouver")
    singapore_tz = pytz.timezone("Asia/Singapore")

    # Current times
    kelowna_time = datetime.now(kelowna_tz).strftime("%Y-%m-%d %H:%M:%S")
    singapore_time = datetime.now(singapore_tz).strftime("%Y-%m-%d %H:%M:%S")

    # Reply message
    message = (
        f"🕒 Current Time:\n\n"
        f"🇨🇦 Kelowna: {kelowna_time}\n"
        f"🇸🇬 Singapore: {singapore_time}"
    )

    await update.message.reply_text(message)

# Main bot runner
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("nowwhattime", nowwhattime))
    app.run_polling()

if __name__ == "__main__":
    main()
