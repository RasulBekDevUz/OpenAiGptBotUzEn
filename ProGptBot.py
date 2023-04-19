import telebot
import openai
from telebot import types
openai.api_key = "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"
bot = telebot.TeleBot(token="5940094354:AAGccSjYaVYuFvfz8Rp40MX2wX8AEJPy_Sg")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5,
)

    
    return response["choices"][0]["text"]


bot.set_my_commands([
    {
        "command": "/chatgpt",
        "description": "Enviar un mensaje al bot para que genere una respuesta utilizando la API de ChatGPT"
    }
])


@bot.message_handler(commands=['start'])
def send_inline(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    settings_button = types.InlineKeyboardButton(text='Admin 🧑‍💻', url='https://t.me/Coder998')
    help_button = types.InlineKeyboardButton(text='Admin info 🔐', url='https://t.me/Coder998_Haqida')
    keyboard.add(settings_button, help_button)
    bot.send_message(message.chat.id, """Assalomu alaykum 🖖

Bizning sun'iy ongga ega bo'lgan @ChatGPT_Ai_UzBot ga hush kelibsiz ❤️‍🔥

🔎 Savolni qancha aniq bersangiz shuncha aniq javob olasiz 

📈 Agarda javobni aniq qlib o'zbek tilida olishni hohlsangiz savol tagiga #uzbek deb yozib qo'yishni maslahat beramz

@ChatGPT_Ai_UzBot Mukkammallik sari olg'a 💎

Savvollar, reklama va majburiy obuna bo'yicha @Coder998 ga murojat qiling 🧑‍💻

Endi esa shunchaki savolni yuboring... 💬""", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def send_help(message):
    # Create the inline keyboard with the button
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Admin 👨‍💻', url='https://t.me/Coder998')
    markup.add(btn)

    # Send the message with the inline keyboard
    bot.send_message(chat_id=message.chat.id, text="""Botdan foydalanishda qiyinchiliklar yuzaga kelayotgan bo'lsa adminstratorga murojat qiling 🧑‍💻""", reply_markup=markup)


@bot.message_handler(func=lambda message: message.chat.type == 'private')
def handle_message(message):
    text = message.text
    
    bot.send_message(chat_id=message.chat.id, text="""Savolingiz qabul qilindi... ⏳
Javobni kuting... ⏰
Javobni olmaguncha keyingi savolni yubormay turing... 💬""")
    bot.send_chat_action(message.chat.id,"typing")
    text = message.text

    
    

    text = message.text
    response = generate_response(text)
    
    bot.send_message(chat_id=message.chat.id, text=response)
    
    


bot.polling()
