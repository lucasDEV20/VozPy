import math
from gtts import gTTS
from playsound import playsound 

audio = 'audio.mp3'
audio2 = 'audio2.mp3'
language = 'pt-br'



sp = gTTS (
    text = 'ok lucas iniciando  ',
    lang = 'pt-br',
)

sa = gTTS (
    text = 'alou pra todo mundo  ',
    lang = 'pt-br',
)



sp.save(audio)
playsound(audio)



sa.save(audio2)
playsound(audio2)



