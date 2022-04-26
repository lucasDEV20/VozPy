"""
Created on Sat Nov  9 19:30:35 2019
@author: Sandro Mesquita
"""

import pyttsx3 
engine = pyttsx3.init()
cars = ["Ford", "Volvo", "BMW"]
coisas = ["Ford", "Volvo", "BMW"]

engine.say("ola lucas sou sua assistente, o que posso fazer por você hoje ?")

#engine.say(cars)


#engine.say("marcar uma reuniao ?")
#engine.say("tocar uma musica ?")

engine.say("escolha dentre as opçoes")

print('''Choice your number
[1] cars
[2] Apple ''')

while True:
    option = int(input('Your option: '))
    if option == 1:
        engine.say("vocÊ escolheu")
        engine.say(cars)
        break
    elif option == 2:
        engine.say("vocÊ escolheu")
        engine.say(coisas)
       
        break
    print('Try again')

engine.runAndWait()
engine.stop()