from telebot import TeleBot
import requests

bot = TeleBot(__name__)
bot.config["api_key"] = "2084467577:AAEubFCpL_iPECUTtJo1UySNRCv3IsuK6x8"


def get_reply(message) -> str:
    message = message.get("text")
    reply = requests.get(f"https://astra-backend-intents.herokuapp.com/{message}").text
    return reply


@bot.route("(?!/).+")
def talk(message) -> None:
    bot.send_message(message["chat"]["id"], get_reply(message))


bot.poll()
