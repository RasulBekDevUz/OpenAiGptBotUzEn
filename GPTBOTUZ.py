import telebot
import openai
from deep_translator import GoogleTranslator
API_TOKEN = '6282929370:AAGvHtTbPGMPoKc47SVW8jVEyHklUMp0Bl4'

openai.api_key="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"

bot = telebot.TeleBot(API_TOKEN)

def get_response(msg):
  completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt=msg,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
  return completion.choices[0].text


matn =f"""
<b>
👋 Assalomu alaykum 

Chatgpt ning UZ versionga

Xush kelibsiz !

Savolingizni yozib yuboring.
</b>
"""
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
     bot.send_message(message.chat.id,matn,parse_mode='html')



@bot.message_handler()
def send_answer(message):
  question=message.text
  alo = bot.send_message(message.chat.id,text="<b>⌛️ Iltimos kuting!</b>",parse_mode='html').message_id
  bot.send_chat_action(message.chat.id, action='typing')
  
  try:
    trs = GoogleTranslator(source='auto', target='uz').translate(get_response(question))
    trsen = GoogleTranslator(source='auto', target='en').translate(get_response(question))
    bot.delete_message(message.chat.id,message_id=alo)
    bot.send_message(message.chat.id,text="<b>"+trs+"</b>",parse_mode='html')
    bot.send_message(message.chat.id,text="<b>"+trsen+"</b>",parse_mode='html')
  except Exception as e:
    bot.delete_message(message.chat.id,message_id=alo)
    bot.send_message(message.chat.id,text=f"<b>Serverdan javob {e} kelmadi !</b>",parse_mode='html')
    

bot.infinity_polling()