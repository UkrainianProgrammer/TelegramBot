# Initial version of my script for updater bot
# must be compiled using Python 3.6.x

import telebot
import config
#import urllib2 as urllib
#from StringIO import StringIO
from PIL import Image
#import json
import requests
from bs4 import BeautifulSoup
from io import BytesIO
#import urllib.request as urllib2

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

def fetch_random(message):
    """
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
    """
    from random import randint
    id = randint(1, 1800)
    url = "http://xkcd.com/" + str(id) + "/info.0.json"
    req = requests.get(url)
    json_data = req.json()
    img_url = json_data["img"]
    comic_info = "Title: {0}\nText: {1}".format(json_data["title"], json_data["transcript"])
    bot.send_message(message.from_user.id, comic_info)
    print (img_url)
    return img_url

def fetch_by_id(message, id):
    url = "http://xkcd.com/" + str(id) + "/info.0.json"
    req = requests.get(url)
    json_data = req.json()
    img_url = json_data["img"]
    comic_info = "Title: {0}\nText: {1}".format(json_data["title"], json_data["transcript"])
    bot.send_message(message.from_user.id, comic_info)
    # print (img_url)
    return img_url

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "random comic":
        img_url = fetch_random(message)
        cont = requests.get(img_url)
        img = Image.open(BytesIO(cont.content)).show()
        bot.send_chat_action(message.from_user.id, 'upload_photo')
    else:
        # display specific comic
        # check if text starts with word comic
        # find comic id
        # fetch comic
        if message.text.startswith("comic"):
            if any(i.isdigit() for i in message.text):
                id = message.text.split()[1]
                img_url = fetch_by_id(message, id)
                cont = requests.get(img_url)
                img = Image.open(BytesIO(cont.content)).show()
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                # bot.send_photo(message.from_user.id, img)
            else:
                print ("Error: id is missing\n")
        else:
            print ("Error: command is invalid\n")

bot.polling(none_stop=True)