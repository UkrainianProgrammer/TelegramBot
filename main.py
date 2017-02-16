# Initial version of my script for updater bot
# must be compiled using Python 2.7.x

import telebot
import config
import urllib2 as urllib
from cStringIO import StringIO
from PIL import Image

bot = telebot.TeleBot(config.token)

#bot.send_message("244646820", "test2")

"""upd = bot.get_updates()
#print upd

latest_upd = upd[-1]
message_from_user = latest_upd.message
print message_from_user
"""

print bot.get_me()
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
    #generate random number
    #construct url based on random id
    #fetch image using xkcd json format
    from random import randint
    id = randint(1, 2000)
    url = "http://xkcd.com/" + str(id) + "/info.0.json"
    img_file = urllib.urlopen(url)
    im = StringIO(img_file.read())
    img = Image.open(im)
    return img



@bot.message_handler(content_types=["text"])
def handle_text(message):
    #answer = "sorry, haven't learnt that yet."
    if message.text == "random comic":
        print("test message")
        comic = fetch_random()
        bot.send_message(message.chat.id, comic)
        #answer = "Hi there"
        #log(message, answer)
        #bot.send_message(message.chat.id, answer)
    """
    elif message.text== "not a test":
        answer = "I know that too."
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "1" or message.text == "2":
        bot.send_message(message.chat.id, "I received either 1 or 2")
    elif message.text == "bot, reply" and str(message.from_user.id) == "244646820":
        bot.send_message(message.chat.id, "id match - yes \nwelcome!")
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    """

bot.polling()