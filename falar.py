"""
Created on Sat Nov  9 19:30:35 2019
@author: Sandro Mesquita
"""

import pyttsx3 
engine = pyttsx3.init()
opt1 = ["Ford", "Volvo", "BMW"]
opt2 = ["Ford", "Volvo", "BMW"]
opt3 = ["Ford", "Volvo", "BMW"]


engine.say("ola lucas sou sua assistente, o que posso fazer por você hoje ?")
engine.say("aaaaaaaaaaaaaaaaaaaaaaaaa hue hueheuheu")

#engine.say(cars)


#engine.say("marcar uma reuniao ?")
#engine.say("tocar uma musica ?")

engine.say("escolha dentre as opçoes"), 

print('''Choice your number
[1] cars
[2] Apple
[3] abelha
[4] sair ''')

while True:
    option = int(input('Your option: '))
    if option == 1:
        engine.say("vocÊ escolheu")
        engine.say(opt1)
        break
    if option == 2:
        engine.say("vocÊ escolheu")
        engine.say(opt3)
        break
    elif option == 3:
        engine.say("vocÊ escolheu")
        engine.say(opt3)
        break
    elif option == 4:
        engine.say("vocÊ escolheu")
        quit( engine.say("encerrando o sistema"))
    
        
    print('Try again')



engine.runAndWait()
engine.stop()