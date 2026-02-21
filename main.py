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
        photo="https://private-user-images.githubusercontent.com/263065291/553065632-ed763fed-a548-47ce-bf8f-05b833e99ce1.jpeg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzE3MTU0ODcsIm5iZiI6MTc3MTcxNTE4NywicGF0aCI6Ii8yNjMwNjUyOTEvNTUzMDY1NjMyLWVkNzYzZmVkLWE1NDgtNDdjZS1iZjhmLTA1YjgzM2U5OWNlMS5qcGVnP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDIyMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAyMjFUMjMwNjI3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9OGJiYzFjZTAwYWYzN2FiZTMyNTM1YmM3ODMzMjhjMTRjMmYzY2RlOWRjZDJlZTlmNjBmNmVhYjgxZGFjNzhjNyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.yJ5942n46b5aHOlZzHuRWRU_wk7oG7Ua71GOeWyncLU"
        caption="""Meu amor, é só realizar o pagamento via PIX abaixo ✨  

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
