from telebot import TeleBot
import requests

bot = TeleBot("2006661177:AAG8sZLX4V5YzUKa_XAehfi2uRY6NgcrK4s")


def get_reply(message) -> str:
    message = message.text
    reply = requests.get(f"https://astra-backend-intents.herokuapp.com/{message}").text
    return reply


@bot.message_handler(func=lambda s: len(s.text) != 0)
def talk(message) -> None:
    bot.send_message(message.chat.id, get_reply(message))


bot.polling()
