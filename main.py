# Initial version of my script for updater bot
# must be compiled using Python 3.6.x

import telebot
import config
#import urllib2 as urllib
#from StringIO import StringIO
from PIL import Image
#import urllib.request as urllib2, json
import requests
from bs4 import BeautifulSoup
from io import BytesIO

bot = telebot.TeleBot(config.token)

print (bot.get_me())

"""
will have 2 command that work as text messages:
random comic - fetch random
comic {id} - fetch id specific comic

additional commands may apply (/start, /help etc.)
"""

"""
 idea: TODO: add comic info to the app screen (title, text etc.)
 TODO: finish main commands and write help documentation using BotFather
"""

def fetch_random():
    # fetching comic page
    from random import randint
    page = requests.get("https://xkcd.com/{}/".format(randint(1, 1800)))

    # parsing page content and looking for img url
    content = page.content
    soup = BeautifulSoup(content, "html.parser")
    image_url = soup.find_all("img")[1]["src"]

    # fixing image url and returning the string
    image_url_complete = "https:" + image_url
    print("https:{}".format(image_url))

    return image_url_complete


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "random comic":
        img_url = fetch_random()
        cont = requests.get(img_url)
        #urllib2.urlopen(cont, 'url_image.png')
        img = Image.open(BytesIO(cont.content)).show() # TODO: try download image and then use send_photo routine
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        #bot.send_photo(message.from_user.id, img)
    else:
        #TODO: display specific comic
        print ("Hello\n")

bot.polling(none_stop=True)