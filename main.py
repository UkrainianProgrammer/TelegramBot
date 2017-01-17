# Initial version of my script for updater bot

import telebot
import config

bot = telebot.TeleBot(config.token)

#bot.send_message("244646820", "test2")

"""upd = bot.get_updates()
#print upd

latest_upd = upd[-1]
message_from_user = latest_upd.message
print message_from_user
"""

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text== "test":
        bot.send_message(message.chat.id, "privet")
    elif message.text== "not a test":
        bot.send_message(message.chat.id, "I know that too.")
    else: bot.send_message(message.chat.id, "sorry, haven't learnt that yet.")

bot.polling(none_stop=True)