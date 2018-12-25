import RPi.GPIO as GPIO
import time

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    pass

def beep():
    GPIO.output(11,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(11,GPIO.HIGH)
    for i in range(1,4):
        GPIO.output(11,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(11,GPIO.HIGH)
        time.sleep(0.1)

def beep1():
    for i in range(1,4):
        GPIO.output(11,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(11,GPIO.HIGH)
        time.sleep(0.1)
init()
beep1()
GPIO.cleanup()
