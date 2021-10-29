from telebot import TeleBot
import requests

bot = TeleBot("2084467577:AAEubFCpL_iPECUTtJo1UySNRCv3IsuK6x8")


def get_reply(message) -> str:
    message = message.text
    reply = requests.get(f"https://astra-backend-intents.herokuapp.com/{message}").text
    return reply


@bot.message_handler(func=lambda s: len(s.text) != 0)
def talk(message) -> None:
    bot.send_message(message.chat.id, get_reply(message))


bot.polling()
