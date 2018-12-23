import RPi.GPIO as GPIO   
import time   
import os

GPIO.setmode(GPIO.BOARD)   
GPIO.setup(11, GPIO.IN)
while True:
    inputValue = GPIO.input(11)
    if inputValue==True:
        print("Button pressed ")
        os.popen('python detect_ed.py')
        time.sleep(0.5)
        while inputValue ==  False:
            time.sleep(0.3)   

