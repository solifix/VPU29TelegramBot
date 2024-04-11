from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton('Share my location', request_location=True)],
        [KeyboardButton('Share my contact', request_contact=True)],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!",
        reply_markup=reply_markup
    )