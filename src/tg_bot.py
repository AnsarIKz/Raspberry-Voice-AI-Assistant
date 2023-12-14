
import telebot
API_TOKEN = '6694847964:AAG-ji0QL2LZ0eH0a-6w6QMHI_PMD14kbgw'
GROUP_ID = -4015373655

bot = telebot.TeleBot(API_TOKEN)

def send_message(msg):
    bot.send_message(GROUP_ID, msg)
