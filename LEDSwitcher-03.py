#!/usr/bin/python
"""

MD20220521-01 LEDSwitcher.py

This code is a sample to test the development of a touch-screen GUI
on a 3.5" LED display on a Raspbeery Pi.

Pyton development of a GUI that works on the 3.5" LED screen on a Raspberry Pi 3B
Note 2 from the MacBook
Note 3 from MacBook
Note 4 from MacBook
Note 5 from RPi
Note 6 from MacBook

"""
from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
# this is a module I defined to alias GPIO numbers to Raspberry Pi pins
import MDRPiGPIO

LEDPin = 40
LEDStatus = False

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# set pin 40 as an output pin, likely to draw some current
GPIO.setup(LEDPin, GPIO.OUT)
# set the initial status of pin 40 to LOW
GPIO.output(LEDPin, GPIO.LOW)

# create a new window called win
win = Tk()

# set the font for the GUI elements
myFont = tkinter.font.Font(family = 'Helvetica', size = 36, weight = 'bold')

# define the ledON function
def ledON():
	# print that the LED On button has been pressed
	print("LED On button pressed")
	# set the status of pin 40 to HIGH
	GPIO.output(LEDPin,GPIO.HIGH)
	LEDStatus = True
	print("LED Status",LEDStatus)
	ledOnButton.pack_forget()
	ledOffButton.pack()

def ledOFF():
	# print that the LED Off button has been pressed
	print("LED Off Button Pressed")
	GPIO.output(LEDPin,GPIO.LOW)
	LEDStatus = False
	print("LED Status",LEDStatus)
	ledOffButton.pack_forget()
	ledOnButton.pack()


# define the exitProgram function
def exitProgram():
	print("Exit Button pressed")
	GPIO.cleanup()
	win.quit()


# set the title of the application window
win.title("LED Switcher")
# set the size of the app (to match the scree size, make this dynamic later)
win.geometry('800x480')

# define a button, called eitButton, and set various parameters
exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6)
exitButton.pack(side = BOTTOM)

# define a button called ledON Button and set various parameters
ledOnButton = Button(win, text = "LED ON", font = myFont, command = ledON, height = 2, width =8 , bg='green')
ledOnButton.pack()

# define a button called ledOFF Button and set various parameters
ledOffButton = Button(win, text = "LED OFF", font = myFont, command = ledOFF, height = 2, width =8 , bg='red')
# ledOffButton.pack()
# ledOffButton.pack_forget()


mainloop()
