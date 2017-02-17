# Initial version of my script for updater bot
# must be compiled using Python 2.7.x

import telebot
import config
#import urllib2 as urllib
from cStringIO import StringIO
from PIL import Image
import urllib, json

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
    #need to parse json to extract image url
    from random import randint
    id = randint(1, 2000)
    print ("id is" + str(id) + "\n")
    url = "http://xkcd.com/" + str(id) + "/info.0.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print data

    #return None



@bot.message_handler(content_types=["text"])
def handle_text(message):
    #answer = "sorry, haven't learnt that yet."
    if message.text == "random comic":
        print("test message\n")
        fetch_random()
        #bot.send_message(message.chat.id, comic)
        #answer = "Hi there"
        #log(message, answer)
        #bot.send_message(message.chat.id, answer)
    else:
        print ("Hello\n")

bot.polling()