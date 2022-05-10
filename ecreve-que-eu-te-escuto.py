import math
from gtts import gTTS
from playsound import playsound 

audio = 'audio.mp3'
audio2 = 'audio2.mp3'
language = 'pt-br'

sp = gTTS (
    text = 'marcelo almeida marcelo almeida marcelo almeida marcelo almeida ',
    lang = 'pt-br'
)

sa = gTTS (
    text = 'você nunca sabera, nunca, desligando ',
    lang = 'pt-br'
)





sp.save(audio)
sa.save(audio2)
playsound(audio)
playsound(audio2)



