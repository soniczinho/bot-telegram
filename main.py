from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

import os

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("🔥 Pack R$25", callback_data="pack")],
        [InlineKeyboardButton("💎 Mensal R$40", callback_data="mensal")],
        [InlineKeyboardButton("👑 Anual R$60", callback_data="anual")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Escolha seu plano 👇", reply_markup=reply_markup)

async def button(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "pack":
        await query.message.reply_text("Você escolheu o Pack! 💸")
    elif query.data == "mensal":
        await query.message.reply_text("Você escolheu o Mensal! 💸")
    elif query.data == "anual":
        await query.message.reply_text("Você escolheu o Anual! 💸")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot rodando...")
app.run_polling()
