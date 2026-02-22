import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

TOKEN = "8481208612:AAHaK9o4iZoJujOurOgs6KuEEz_Js6emUNE"  # seu token do BotFather

# Arquivo que vai salvar os usuários
ARQUIVO_USUARIOS = "usuarios.json"

# Função para salvar plano do usuário
def salvar_usuario(user_id, plano):
    try:
        with open(ARQUIVO_USUARIOS, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data[str(user_id)] = plano

    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(data, f, indent=4)

# Função /start
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
        photo="https://files.catbox.moe/za2jqx.jpg",  # link direto da imagem
        caption="""Meu amor, é só realizar o pagamento via PIX abaixo ✨

Confirmou, o acesso é liberado 🔥

Escolha um dos planos abaixo 👇""",
        reply_markup=reply_markup
    )

# Função que trata clique nos botões
async def botao(update, context):
    query = update.callback_query
    await query.answer()

    escolha = query.data
    user_id = query.from_user.id

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

    # Salva automaticamente o usuário e o plano escolhido
    salvar_usuario(user_id, plano)

    await query.message.reply_text(
        f"""💰 Plano escolhido: {plano}

Valor: {valor}

Pix: 82b450d2-c9a4-44af-8577-914677d13c19

Após pagar, envie o comprovante aqui."""
    )

# Inicialização do bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(botao))

app.run_polling()
