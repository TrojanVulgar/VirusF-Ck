from gtts import gTTS
import os

msg = 'Fuck your system'
language = 'en'

obj=gTTS(text=msg, lang=language, slow=False)

obj.save('Virus.mp4')

while True:
os.system('mpg321 Virus.mp4')