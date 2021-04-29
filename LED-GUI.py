from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Setup
red = 11
amber = 13
blue = 15
GPIO.setup(red, GPIO.OUT)
GPIO.setup(amber, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)


# Definitions
win = Tk()
win.title("LED Buttons")
myFont = tkinter.font.Font(family = 'Courier', size = 11)
win.radioVar = IntVar()

# Functions
def toggleLed():
    if win.radioVar.get() == 2:
        GPIO.output(red, GPIO.LOW)
        GPIO.output(amber, GPIO.HIGH)
        GPIO.output(blue, GPIO.LOW)
    elif win.radioVar.get() == 3:
        GPIO.output(red, GPIO.LOW)
        GPIO.output(amber, GPIO.LOW)
        GPIO.output(blue, GPIO.HIGH)
    else:
        GPIO.output(red, GPIO.HIGH)
        GPIO.output(amber, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)
    
def close():
    GPIO.cleanup()
    win.destroy()
    
# Widgets
redButton = Radiobutton(win, text = "Red LED", variable=win.radioVar, value=1, font = myFont, command = toggleLed, height = 3, width = 30)
redButton.grid(row=0, column=1)

amberButton = Radiobutton(win, text = "Amber LED", variable=win.radioVar, value=2, font = myFont, command = toggleLed, height = 3, width = 30)
amberButton.grid(row=1, column=1)

blueButton = Radiobutton(win, text = "Blue LED", variable=win.radioVar, value=3, font = myFont, command = toggleLed, height = 3, width = 30)
blueButton.grid(row=2, column=1)

exitButton = Button(win, text = "Exit", font = myFont, command=close, height = 3, width = 30)
exitButton.grid(row=3, column=1)

    
win.protocol("WM_DELETE_WINDOW", close)

# Loop
win.mainloop()