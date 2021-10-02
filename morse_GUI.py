from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

### hardware
red = LED(25)

### GUI definitions ###
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica',size=12,weight = "bold")

### Event Function ###

def enter_text():
    input = inputer.get("1.0", "end-1c")
    outputer.config(text=input)

### Widgets ###
inputer = Text(win, height = 2, width = 24,bg = "light yellow")
outputer = Label(win, height = 2, width = 24,bg = "bisque1")
red_btn = Button(win,text = "Enter",font = myFont, command = enter_text,bg = 'bisque2',height = 1,width =12)
exit_btn = Button(win,text = "Exit",font = myFont, command = win.destroy,bg = 'red',height = 1,width =12)

inputer.grid(row=1,column=1, padx=6,pady=6)
outputer.grid(row=1,column=2, padx=6,pady=6)
red_btn.grid(row=3,column=1, padx=6,pady=6)
exit_btn.grid(row=3,column=2, padx=6,pady=6)


