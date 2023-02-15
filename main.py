import telebot
import requests

bot = telebot.TeleBot('6240377442:AAHmnnqh2Qe32uxQlCe-oQwR2mlqPwv4MBQ')

# заставить бота обрабатывать сообщения (хэндлеры/обработчики)
@bot.message_handler(commands=['start', 'help'])
def greeting(message):
    bot.send_message(message.chat.id, 'Это успокаивающий бот. Он умеет отправлять картинки котиков, собачек и космоса!')
    bot.send_message(message.chat.id, '/randomdog - чтобы получить картинку собачки,\n/randomcat - чтобы получить '
                                      'картинку котика,\n/dailyspace - чтобы получить картинку космоса')

# команды, которые будутотлавливать команды, которые пользователь отправляет боту:
@bot.message_handler(commands=['randomdog'])
def rand_dog(message):
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']
    bot.send_photo(message.chat.id, photo=image_url)

@bot.message_handler(commands=['randomcat'])
def rand_cat(message):
    contents = requests.get('https://api.thecatapi.com/v1/images/search').json()
    image_url = contents[0]['url']
    bot.send_photo(message.chat.id, photo=image_url)

@bot.message_handler(commands=['dailyspace'])
def space(message):
    print(message)
    URL = 'https://api.nasa.gov/planetary/apod?api_key=lGmCcQ6mnvCVUUEHHSpS4w1SD3zHFPmr31Bws76o'
    print(URL)
    contents = requests.get(URL).json()
    image_url = contents['url']
    print(image_url)
    bot.send_photo(message.chat.id, photo=image_url)

# чтобы получать сообщения от пользователя:
bot.polling(none_stop=True)
