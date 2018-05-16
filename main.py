from gtts import gTTS
import time
import telepot
from telepot.loop import MessageLoop
import os




def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    if command == "/start":
        bot.sendMessage(chat_id, "Салам, Кенжегали, я слушаю")
    else:
        print(command)
        tts = gTTS(str(command), lang='ru')
        tts.save('simple.mp3')
        bot.sendDocument(chat_id, open('simple.mp3', 'rb'))
        os.remove('simple.mp3')




TOKEN = '557066844:AAGf63b9XwMwpYZ-oiWfH22MY9fksFkc3mo'  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

# Keep the program running.
while 1:
    time.sleep(10)

