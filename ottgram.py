import sys
import time
import telepot
from pprint import pprint

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        pprint(msg)
        text = msg['text']
        if text == '...':
            bot.sendMessage(chat_id, 'FUCK YOU!!')
        else:
            bot.sendMessage(chat_id, '...')
    elif content_type == 'photo':
        pprint(msg)



TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)