import RPi.GPIO as GPIO   
import time   
import os

GPIO.setmode(GPIO.BOARD)   
GPIO.setup(11, GPIO.IN)
while True:
    inputValue = GPIO.input(11)
    if inputValue==True:
        print("Button pressed ")
        os.popen('./remoteStart.sh')
        os.popen('sudo python detect_ed.py > /dev/null &')
        os.popen('sudo python ble_scan_v4.py >/dev/null &')
        time.sleep(0.5)
        while inputValue ==  False:
            time.sleep(0.3)   

