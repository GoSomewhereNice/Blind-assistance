import RPi.GPIO as GPIO
import time

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.IN)
    GPIO.setup(11,GPIO.OUT)
    pass

def beep():
    for i in range(1,6):
        GPIO.output(11,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(11,GPIO.HIGH)
        time.sleep(0.5)
        print "The Buzzer will make sound"

def beep1():
    for i in range(1,3):
        GPIO.output(11,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(11,GPIO.HIGH)
        time.sleep(0.2)
        print "CLOSING Sound!!!"

def detect():
    for i in range(1,31):
        j = 0
        if GPIO.input(12) == False and j < 3:
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"  Guide Beep~"
            beep()
        else:
            GPIO.output(11,GPIO.HIGH)
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"  Closing Beep~"
            beep1()
            j+=1
        time.sleep(3)
time.sleep(2)
init()
detect()
GPIO.cleanup()
