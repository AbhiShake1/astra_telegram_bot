from telebot import TeleBot
import requests

API_KEY = "2084467577:AAEubFCpL_iPECUTtJo1UySNRCv3IsuK6x8"

bot = TeleBot(API_KEY)


def get_reply(message) -> str:
    message = message.text
    reply = requests.get(f"https://astra-backend-intents.herokuapp.com/{message}")
    return reply.text


@bot.message_handler(commands=["about"])
def talk_about_bot(message):
    bot.reply_to(message, "I'm Astra. I was created by Abhi. "
                          "My name and behaviour is inspired by Astrid S who is the favourite singer of Abhi.")


@bot.message_handler(func=lambda _: True)
def talk(message):
    bot.send_message(message.chat.id, get_reply(message))


bot.polling()
