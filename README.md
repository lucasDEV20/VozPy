# VozPy
sistema de voz e afins em python
## instale as seguintes bibliotecas 

" pip install SpeechRecognition "
" pip install pyaudio "
--
 A biblioteca speech recognition possui a dependencia com a biblioteca PyAudio, por isso também precisamos instalá-la, com o comando.
--

## Codigo fonte 

import speech_recognition as sr
#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
 #Habilita o microfone para ouvir o usuario
 microfone = sr.Recognizer()
 with sr.Microphone() as source:
  #Chama a funcao de reducao de ruido disponivel na speech_recognition
  microfone.adjust_for_ambient_noise(source)
  #Avisa ao usuario que esta pronto para ouvir
  print("Diga alguma coisa: ")
  #Armazena a informacao de audio na variavel
  audio = microfone.listen(source)
try:
  #Passa o audio para o reconhecedor de padroes do speech_recognition
  frase = microfone.recognize_google(audio,language='pt-BR')
  #Após alguns segundos, retorna a frase falada
  print("Você disse: " + frase)
#Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
 except sr.UnkownValueError:
  print("Não entendi")
return frase
ouvir_microfone()

----------------------------------------------------------------

## VozPyGoogle
scrpt de leitura com a voz do google 

## instale as seguintes biblioteca

pip install gTTS
pip install playsound

## Codigo fonte 

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
#Funcao responsavel por falar 
def cria_audio(audio):
 tts = gTTS(audio,lang='pt-br')
 #Salva o arquivo de audio
 tts.save('audios/hello.mp3')
 print("Estou aprendendo o que você disse...")
 #Da play ao audio
 playsound('audios/hello.mp3')
#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
 #Habilita o microfone para ouvir o usuario
 microfone = sr.Recognizer()
 with sr.Microphone() as source:
  #Chama a funcao de reducao de ruido disponivel na speech_recognition
  microfone.adjust_for_ambient_noise(source)
  #Avisa ao usuario que esta pronto para ouvir
  print("Diga alguma coisa: ")
  #Armazena a informacao de audio na variavel
  audio = microfone.listen(source)
try:
  #Passa o audio para o reconhecedor de padroes do speech_recognition
  frase = microfone.recognize_google(audio,language='pt-BR')
  #Após alguns segundos, retorna a frase falada
  print("Você disse: " + frase)
#Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
 except sr.UnkownValueError:
  print("Não entendi")
return frase
frase = ouvir_microfone()
cria_audio(frase)


---------------------------------
## ecreve-que-eu-te-escuto

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




