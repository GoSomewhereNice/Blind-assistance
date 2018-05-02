import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 2 
ECHO = 3
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)

while GPIO.input(ECHO) == 0 :
    pass
pulse_start = time.time()

while GPIO.input(ECHO) == 1 :
    pass
pulse_end = time.time()

pulse_duration = pulse_end - pulse_start 
distance = pulse_duration * 17150
distance = round(distance,1)
print("Distance: {}cm".format(distance))
GPIO.cleanup()
