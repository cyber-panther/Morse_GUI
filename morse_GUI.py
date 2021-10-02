from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

### variables ###
code = "| "

### hardware
red = LED(25)

### GUI definitions ###
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica',size=12,weight = "bold")

### Event Function ###

def dot():
    global code
    code = code + ". "
    red.on()
    time.sleep(0.5)
    red.off()
    time.sleep(0.5)    

def dash():
    global code
    code = code + "- "
    red.on()
    time.sleep(1.0)
    red.off()
    time.sleep(0.5)  

def blinkMorseSet(Input):

    for letter in Input:
        if (letter == 'a'):
            dot()
            dash()

        elif (letter == 'b'):
            dash()
            dot()
            dot()
            dot()

        elif (letter == 'c'):
            dash()
            dot()
            dash()
            dot()

        elif (letter == 'd'):
            dash()
            dot()
            dot()

        elif (letter == 'e'):
            dot()

        elif (letter == 'f'):
            dot()
            dot()
            dash()
            dot()

        elif (letter == 'g'):
            dash()
            dash()
            dot()

        elif (letter == 'h'):
            dot()
            dot()
            dot()
            dot()

        elif (letter == 'i'):
            dot()
            dot()

        elif (letter == 'j'):
            dot()
            dash()
            dash()
            dash()

        elif (letter == 'k'):
            dash()
            dot()
            dash()

        elif (letter == 'l'):
            dot()
            dash()
            dot()
            dot()

        elif (letter == 'm'):
            dash()
            dash()

        elif (letter == 'n'):
            dash()
            dot()

        elif (letter == 'o'):
            dash()
            dash()
            dash()

        elif (letter == 'p'):
            dot()
            dash()
            dash()
            dot()

        elif (letter == 'q'):
            dash()
            dash()
            dot()
            dash()

        elif (letter == 'r'):
            dot()
            dash()
            dot()

        elif (letter == 's'):
            dot()
            dot()
            dot()

        elif (letter == 't'):
            dash()

        elif (letter == 'u'):
            dot()
            dot()
            dash()

        elif (letter == 'v'):
            dot()
            dot()
            dot()
            dash()

        elif (letter == 'w'):
            dot()
            dash()
            dash()

        elif (letter == 'x'):
            dash()
            dot()
            dot()
            dash()

        elif (letter == 'y'):
            dash()
            dot()
            dash()
            dash()

        elif (letter == 'z'):
            dash()
            dash()
            dot()
            dot()
        
        global code
        code = code + " | "

def enter_text():
    input = inputer.get("1.0", "end-1c")
    
    if(len(input)>12):
        outputer.config(text="Please input less characters")
        return
    blinkMorseSet(input)
    
    global code
    outputer.config(text=code)
    code = "| "
    
### Widgets ###
inputer = Text(win, height=2, width=48, bg="light yellow")
outputer = Label(win, height=2, width=48, bg="bisque1")
enter = Button(win, text="Enter", font=myFont,
                 command=enter_text, bg='bisque2', height=2, width=24)
exit_btn = Button(win, text="Exit", font=myFont,
                  command=win.destroy, bg='red', height=2, width=24)

inputer.grid(row=1, column=1, padx=16, pady=12)
outputer.grid(row=3, column=1, padx=16, pady=12)
enter.grid(row=2, column=1, padx=12, pady=12)
exit_btn.grid(row=4, column=1, padx=12, pady=12)

win.mainloop()
