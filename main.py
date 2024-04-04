import os
import logging

from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()

TELEGRAM_TOKEN_BOT = os.getenv('TELEGRAM_TOKEN_BOT')

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [KeyboardButton('Hello'), KeyboardButton('Word')],
        [KeyboardButton('Good buy')],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f'Привіт {update.effective_user.first_name}',
        reply_markup=reply_markup)


async def author(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Мене робив Diduh Andrian")

async def Bye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="пращавай")


app = ApplicationBuilder().token(TELEGRAM_TOKEN_BOT).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("author", author))
app.add_handler(CommandHandler("Bye", Bye))

app.run_polling()
