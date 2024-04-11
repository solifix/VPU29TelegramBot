from telegram import Update
from telegram.ext import ContextTypes


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lat = update.message.location.latitude
    lon = update.message.location.longitude

    await update.message.reply_text(f'lat = {lat}, lon = {lon}')