from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

TOKEN = "8481208612:AAHaK9o4iZoJujOurOgs6KuEEz_Js6emUNE"

# /start
async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("💎 Semanal R$20", callback_data="semanal")],
        [InlineKeyboardButton("🔥 Mensal R$32", callback_data="mensal")],
        [InlineKeyboardButton("👑 3 Meses R$42,90", callback_data="3meses")],
        [InlineKeyboardButton("💖 Vitalício R$59,99", callback_data="vitalicio")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="https://raw.githubusercontent.com/soniczinho/bot-telegram/refs/heads/main/foto.jpeg"

Confirmou, o acesso é liberado 🔥  

Escolha um dos planos abaixo 👇""",
        reply_markup=reply_markup
    )

# clique nos botões
async def botao(update, context):
    query = update.callback_query
    await query.answer()

    escolha = query.data

    if escolha == "semanal":
        plano = "Semanal"
        valor = "R$20"
    elif escolha == "mensal":
        plano = "Mensal"
        valor = "R$32"
    elif escolha == "3meses":
        plano = "3 Meses"
        valor = "R$42,90"
    elif escolha == "vitalicio":
        plano = "Vitalício"
        valor = "R$59,99"
    else:
        return

    await query.message.reply_text(
        f"""💰 Plano escolhido: {plano}

Valor: {valor}

Pix: 82b450d2-c9a4-44af-8577-914677d13c19

Após pagar, envie o comprovante aqui."""
    )

# iniciar bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(botao))

app.run_polling()
