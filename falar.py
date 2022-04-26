"""
Created on Sat Nov  9 19:30:35 2019
@author: Sandro Mesquita
"""

import pyttsx3 
engine = pyttsx3.init()
cars = ["Ford", "Volvo", "BMW"]

engine.say("ola lucas sou sua assistente, o que posso fazer por você hoje ?")

#engine.say(cars)


#engine.say("marcar uma reuniao ?")
#engine.say("tocar uma musica ?")


print('''Choice your number
[1] Banana
[2] Apple ''')
engine.say("escolha dentre as opçoes")
while True:
    option = int(input('Your option: '))
    if option == 1:
        engine.say("voce escolheu banana")
        print('Banana choiced')
        break
    elif option == 2:
        engine.say("voce escolheu maça")
        print('Apple choiced')
        break
    print('Try again')

engine.runAndWait()
engine.stop()