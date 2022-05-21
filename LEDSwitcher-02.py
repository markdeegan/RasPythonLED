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

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# set pin 40 as an output pin, likely to draw some current
GPIO.setup(40, GPIO.OUT)
# set the initial status of pin 40 to LOW
GPIO.output(40, GPIO.LOW)

# create a new window called win
win = Tk()

# set the font for the GUI elements
myFont = tkinter.font.Font(family = 'Helvetica', size = 36, weight = 'bold')

# define the ledON function
def ledON():
	# print that the LED button has been pressed
	print("LED button pressed")
	# check the status of pin 40, and respond accordingly
	# if it is HIGH, then
	if GPIO.input(40):
		# set status of pin 40 to LOW and
		GPIO.output(40,GPIO.LOW)
		# change the text displayed by the button to LED ON
		ledButton["text"] = "LED ON"
	# if it is LOW (else) then
	else:
		# set status of pin 40 to LOW and
		GPIO.output(40,GPIO.HIGH)
		# change the text displayed by the button to LED OFF
		ledButton["text"] = "LED OFF"

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

# define a button called ledButton and set various parameters
ledButton = Button(win, text = "LED 1 ON", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack(side = LEFT)

# define a button called ledButton and set various parameters
ledButton2 = Button(win, text = "LED 2 ON", font = myFont, command = ledON, height = 2, width =8 )
ledButton2.pack(side = RIGHT)

mainloop()
