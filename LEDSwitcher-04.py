#!/usr/bin/python
"""

MD20220527-01 LEDSwitcher-04.py

This code is a sample to test the development of a touch-screen GUI
on a 3.5" LED display on a Raspbeery Pi.

Pyton development of a GUI that works on the 3.5" LED screen on a Raspberry Pi 3B

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

# set LEDpin (40) as an output pin, likely to draw some current
GPIO.setup(LEDPin, GPIO.OUT)
# set the initial status of LEDPin(40) to LOW
GPIO.output(LEDPin, GPIO.LOW)

# create a new window called win
win = Tk()
# set the title of the application window
win.title("LED Switcher")
# set the size of the app (to match the scree size, make this dynamic later)
win.geometry('800x480')

# set the font for the GUI elements
myFont = tkinter.font.Font(family = 'Helvetica', size = 36, weight = 'bold')

#####################
# define the exitProgram function
def exitProgram():
	print("Exit Button pressed")
	GPIO.cleanup()
	win.quit()

##########################################
# define the ledON function
def ledON():
	# print that the LEDOn button has been pressed
	print("LED On button pressed")
	# set the status of the relevant pin to HIGH
	GPIO.output(LEDPin, GPIO.HIGH)
	# and flip the status boolean, which should always map the relevant pin
	LEDStatus = True
	# diagnostics message
	print("LED Status", LEDStatus)
	# hide the ledOnButton
	ledOnButton.pack_forget()
	# show the ledOffButton
	ledOffButton.pack()

##########################################
# define the ledOff function
def ledOFF():
	# print that the LEDOff button has been pressed
	print("LED Off Button Pressed")
	# set the status of the relevant pin to LOW
	GPIO.output(LEDPin, GPIO.LOW)
	# and flip the status boolean, which should always map the relevant pin
	LEDStatus = False
	# diagnostics message
	print("LED Status", LEDStatus)
	# hide the ledOffButton
	ledOffButton.pack_forget()
	# show the ledOnButton
	ledOnButton.pack()


# define a button, called eitButton, and set various parameters
exitButton  = tkinter.Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6)
exitButton.pack(side = BOTTOM)

# define a button called ledON Button and set various parameters
ledOnButton = tkinter.Button(win, text = "LED ON", font = myFont, command = ledON, height = 2, width =8)
ledOnButton.pack()

# define a button called ledOFF Button and set various parameters
ledOffButton = tkinter.Button(win, text = "LED OFF", font = myFont, command = ledOFF, height = 2, width =8)

mainloop()
