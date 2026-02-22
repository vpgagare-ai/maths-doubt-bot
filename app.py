import os
import telebot
from openai import OpenAI

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    user_question = message.text

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a maths teacher. Explain step by step in Marathi and English. Also give 2 similar practice questions."},
            {"role": "user", "content": user_question}
        ]
    )

    bot.reply_to(message, response.choices
