import telebot
import webbrowser

bot = telebot.TeleBot('6377876474:AAFhW125c7MJvnBke0AyFu2YPQ8Xo_Ej_tY')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://ya.ru')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    print("Success send message start!")


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')
    print("Success send message help!")


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.infinity_polling()
