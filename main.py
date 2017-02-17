# Initial version of my script for updater bot
# must be compiled using Python 3.6.x

import telebot
import config
#import urllib2 as urllib
#from cStringIO import StringIO
#from PIL import Image
import urllib.request as urllib2, json
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.token)

#bot.send_message("244646820", "test2")

"""upd = bot.get_updates()
#print upd

latest_upd = upd[-1]
message_from_user = latest_upd.message
print message_from_user
"""

print (bot.get_me())
"""
def log(message, answer):
    print "\n -----------"
    from datetime import datetime
    print datetime.now()
    print "Message from {0} {1}. (id = {2}) \n Text: {3}".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text)
    print answer

"""

"""
will have 2 command that work as text messages:
random comic - fetch random
comic {id} - fetch id specific comic

additional commands may apply (/start, /help etc.)
"""


def fetch_random():
    from random import randint
    page = requests.get("https://xkcd.com/{}/".format(randint(1, 1800)))
    content = page.content
    soup = BeautifulSoup(content, "html.parser")
    image_url = soup.find_all("img")[1]["src"]
    image_url_complete = "https:" + image_url
    print("https:{}".format(image_url))
    return (image_url_complete)

    """
    # generate random number
    from random import randint
    id = randint(1, 2000)
    print ("id is " + str(id) + "\n")

    # construct url based on random id
    url = "http://xkcd.com/" + str(id) + "/info.0.json"

    # fetch image using xkcd json format
    # need to parse json to extract image url
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = json.loads(response.read())
    #print data
    img_url = data["img"]
    print img_url
    return img_url
    # return opened image (?)
"""

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "random comic":
        #context = ssl._create_unverified_context()
        #print("test message\n")
        img_url = fetch_random()

        #req = urllib2.Request(img_url)
        resp = urllib2.urlopen(img_url, 'url_image.png')
        img = open('url_image.png')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    else:
        print ("Hello\n")

bot.polling()