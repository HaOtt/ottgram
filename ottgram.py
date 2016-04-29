import sys
import time
import telepot
from PIL import Image


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        text = msg['text']
        if text == '...':
            bot.sendMessage(chat_id, 'FUCK YOU!!')
        else:
            bot.sendMessage(chat_id, '...')
    elif content_type == 'photo':
        photo = msg['photo'][3]['file_id']
        fp = 'ottgram_image.jpg'
        bot.download_file(photo, fp)
        im = Image.open(fp)
        im.rotate(180).save(fp)
        f = open(fp, 'rb')
        bot.sendPhoto(chat_id, f)
        f.close()

TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)