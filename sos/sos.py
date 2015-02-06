#SOS flasher by Harry Taylor

import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BOARD) #set the pin numbering system

GPIO.setup(11,GPIO.OUT)

#function definition

#Defines a dot in the program (when 'e' is written, it will change to one dot)
def dot():
        print('.', end="")
        GPIO.output(11,False)
        time.sleep(0.5)
        GPIO.output(11,True)
        time.sleep(0.5)
	

#Defines a dash in the program (when 'a' is written, it will change to '.-'
def dash():
        print('_', end="")
        GPIO.output(11,False)
        time.sleep(1)
        GPIO.output(11,True)
        time.sleep(0.5)

#GPIO.output(11,True)
#time.sleep(1)

def morseletter(letter):
    if letter == "a":   
        dot()
        dash()
    elif letter == "b":
        dash()
        dot()
        dot()
        dot()
    elif letter == "c":
        dash()
        dot()
        dash()
        dot()
    elif letter == "d":
        dash()
        dot()
        dot()
    elif letter == "e":
        dot()
    elif letter == "f":
        dot()
        dot()
        dash()
        dot()
    elif letter == "g":
        dash()
        dash()
        dot()
    elif letter == "h":
        dot()
        dot()
        dot()
        dot()
    elif letter == "i":
        dot()
        dot()
    elif letter == "j":
        dot()
        dash()
        dash()
        dash()
    elif letter == "k":
        dash()
        dot()
        dash()
    elif letter == "l":
        dot()
        dash()
        dot()
        dot()
    elif letter == "m":
        dash()
        dash()
    elif letter == "n":
        dash()
        dot()
    elif letter == "o":
        dash()
        dash()
        dash()
    elif letter == "p":
        dot()
        dash()
        dash()
        dot()
    elif letter == "q":
        dash()
        dash()
        dot()
        dash()
    elif letter == "r":
        dot()
        dash()
        dot()
    elif letter == "s":
        dot()
        dot()
        dot()
    elif letter == "t":
        dash()
    elif letter == "u":
        dot()
        dot()
        dash()
    elif letter == "v":
        dot()
        dot()
        dot()
        dash()
    elif letter == "w":
        dot()
        dash()
        dash()
    elif letter == "x":
        dash()
        dot()
        dot()
        dash()
    elif letter == "y":
        dash()
        dot()
        dash()
        dash()
    elif letter == "z":
        dash()
        dash()
        dot()
        dot()

    elif letter == "1":
        dot()
        dash()
        dash()
        dash()
        dash()
    elif letter == "2":
        dot()
        dot()
        dash()
        dash()
        dash()
    elif letter == "3":
        dot()
        dot()
        dot()
        dash()
        dash()
    elif letter == "4":
        dot()
        dot()
        dot()
        dot()
        dash()
    elif letter == "5":
        dot()
        dot()
        dot()
        dot()
        dot()
    elif letter == "6":
        dash()
        dot()
        dot()
        dot()
        dot()
    elif letter == "7":
        dash()
        dash()
        dot()
        dot()
        dot()
    elif letter == "8":
        dash()
        dash()
        dash()
        dot()
        dot()
    elif letter == "9":
        dash()
        dash()
        dash()
        dash()
        dot()
    elif letter == "0":
        dash()
        dash()
        dash()
        dash()
        dash()

message = input("What letter(s)/number(s) would you like to see in morse? ")
for each in message:
        morseletter(each)













        
