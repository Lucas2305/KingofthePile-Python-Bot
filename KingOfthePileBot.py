import random
import requests
from bs4 import BeautifulSoup
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(10)

#loooooooooooooooooooooooooooooooooooooooooop!
while 1 != 2:
 #webscraping with python. Put the ip address into the url !   
    url = 'http://<ip address>/pileking/'
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")                      

    print (content)

    nugget = content.findAll(iframe, attrs={"scr": "content"}).text

    print (nugget)
#delay to make it easyer and without any controll (maybe something in 2.0)
    time.sleep(3)


#possible character (I was to lazy to type out the abc)
    AA = {"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"}
    BB = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"}
    CC = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"}
    DD = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"}
    EE = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"}
#part 1 of the output
    keyA = random.choice(list(AA))
    keyB = random.choice(list(BB))
    keyC = random.choice(list(CC))
    keyD = random.choice(list(DD))
    keyE = random.choice(list(EE))
#part 2 of the output
    keyA2 = random.choice(list(AA))
    keyB2 = random.choice(list(BB))
    keyC2 = random.choice(list(CC))
    keyD2 = random.choice(list(DD))
    keyE2 = random.choice(list(EE))
#part 3 of the output
    keyA3 = random.choice(list(AA))
    keyB3 = random.choice(list(BB))
    keyC3 = random.choice(list(CC))
    keyD3 = random.choice(list(DD))
    keyE3 = random.choice(list(EE))
#part 4 of the output
    keyA4 = random.choice(list(AA))
    keyB4 = random.choice(list(BB))
    keyC4 = random.choice(list(CC))
    keyD4 = random.choice(list(DD))
    keyE4 = random.choice(list(EE))
#part 5 of the output
    keyA5 = random.choice(list(AA))
    keyB5 = random.choice(list(BB))
    keyC5 = random.choice(list(CC))
    keyD5 = random.choice(list(DD))
    keyE5 = random.choice(list(EE))

#keyboard emulation with pynput    
       
    keyboard.type("echo" + " " + keyA + keyB + keyC + keyD + keyE + " " + keyA2 + keyB2 + keyC2 + keyD2 + keyE2 + " " + keyA3 + keyB3 + keyC3 + keyD3 + keyE3 + " " + keyA4 + keyB4 + keyC4 + keyD4 + keyE4 + " " + keyA5 + keyB5 + keyC5 + keyD5 + keyE5 + " " + "> " + str(nugget))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

  

    


