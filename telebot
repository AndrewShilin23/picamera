import telebot

TOKEN = '5368571475:AAEX0MZ4_QY2itTWeJj-hSBhWjBUDzZrY1I'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) 
def start(message):
    chatid = message.chat.id
    bot.send_message(chatid,'hi')
    #photo = open('images.png', 'rb')
    #bot.send_photo(chatid, photo)
   

bot.polling(none_stop=True)  
