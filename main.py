from telegram.ext import ApplicationBuilder, CommandHandler

import os

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    await update.message.reply_text("Bot funcionando 👀")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot rodando...")
app.run_polling()