import telebot  

TOKEN = "8112870100:AAH5w-mqJIxXu-39yWQkxR2wGXj1Ij2lDOY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я echo-бот. Надішли мені будь-яке повідомлення, і я повторю його. 🇺🇦")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ти сказав: {message.text}")


if __name__ == "__main__":
    print("Бот запущено! Натисни Ctrl+C для зупинки.")
    bot.polling(none_stop=True)