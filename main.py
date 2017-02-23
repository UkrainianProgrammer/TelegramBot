# Initial version of my script for updater bot
# must be compiled using Python 3.6.x

# a few lines of code were borrowed from
# https://github.com/1995eaton/xkcd_downloader/blob/master/xkcd_downloader.py


import telebot
import config
import requests
#from bs4 import BeautifulSoup
from re import search
import os


bot = telebot.TeleBot(config.token)

# for testing only
print (bot.get_me())

"""
have two commands that work as text messages:
random comic - fetch random
comic {id} - fetch id specific comic

additional commands apply (/start, /help)
"""

"""
 idea: fetch comic by name (?)
 TODO: add custom keyboard (!)
"""

#def fetch_random(message):
    #from random import randint
    #id = randint(1, 1800)
    #return display_image(message, id)

#def fetch_by_id(message, id):
    #return display_image(message, id)

# display random or id-specific comic routine called in handle_text
def display_image(message, id):
    # construct json url
    url = "http://xkcd.com/" + str(id) + "/info.0.json"
    req = requests.get(url)

    # checking status code to make sure request was successful
    if req.status_code != 200:
        print("Error retrieving page.\n")
        return

    print(req.status_code)
    print(url)


    #fetch json file
    json_data = req.json()
    img_url = json_data["img"] # corresponding image url string

    # print comic info
    comic_info = "Title: {0}\nComic ID: {1}\nSummary: {2}".format(json_data["title"], json_data["num"],
                                                                    json_data["alt"])
    bot.send_message(message.from_user.id, comic_info)
    #print(img_url)

    # this is comic image dir
    directory = "/Users/Alex/Documents/GitHub Folders/TelegramBot/img"

    # the section below is borrowed another GitHub repo (link above)
    num = str(json_data['num'])
    image = num + search("\.([a-z])+$", json_data['img']).group()

    with open(directory + '/' + image, 'wb') as image_file:
        req = requests.get(img_url, stream=True) # bypass ssl verification
        for block in req.iter_content(1024):
            if block:
                image_file.write(block)
                image_file.flush()

    # open pic and send it to the app
    img = open(directory + '/' + image, 'rb')
    bot.send_chat_action(message.from_user.id, "upload_photo")
    bot.send_photo(message.from_user.id, img)
    img.close()

    # remove image from server
    os.chdir(directory)
    for file in os.listdir(directory):
        if file.endswith(".jpg") | file.endswith(".png"):
            os.remove(file)


# ----------------------------------------------------------- #

# decorators:

# start and help commands (equivalent for now)
@bot.message_handler(commands=["start", "help"])
def handle_text(message):
    help_string = "Thank you for using xkcd bot for Telegram.\nUse the following commnds:" \
                  "\nrandom comic - view random comic\n" \
                  "comic {id} - view id-specific comic"
    bot.send_message(message.from_user.id, help_string)

# all bot commands
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.lower() == "random comic":
        from random import randint
        id = randint(1, 1900)
        display_image(message, id)
    else:
        # display specific comic
        # check if text starts with word comic
        # find comic id
        # fetch comic
        if message.text.lower().startswith("comic"):
            if any(i.isdigit() for i in message.text):
                id = message.text.split()[1]
                if id == "404":
                    bot.send_message(message.from_user.id, "The comic does not exist.")
                else:
                    display_image(message, id)
            else:
                bot.send_message(message.from_user.id, "Please specify id of the comic. For example: comic 45")
                #print ("Error: id is missing\n")
        else:
            bot.send_message(message.from_user.id, "Invalid command, please use /help to learn more.")
            #print ("Invalid command, please use /help to learn more."\n")


# run the bot
bot.polling(none_stop=True)

#if '__name__' == '__main__':
    #main()