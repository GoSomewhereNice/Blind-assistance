#Project: Parking sensors
#RaspberryyPi 3 Model B+
#Hardware: LED*3(green,yellow,red), 1K-resistance*4, 2K-resistance*1, buzzer*1
#IC: HC-SR04 Ultrasonic Ranging Module
#Editor: NORTHPC

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

echo_pin=18
trigger_pin=16
BUZZER_pin=12

GPIO.setup(trigger_pin, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(BUZZER_pin, GPIO.OUT)
pwm_buzzer = GPIO.PWM(BUZZER_pin,523) #freq=523 Melody DO
pwm_buzzer.start(0) #pwm start as dutycycle=0

v=343 #331+0.6T, T=Celsius

def detection():
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)#10u seconds TTL Trigger Single
    GPIO.output(trigger_pin, GPIO.LOW)
    pulse_start=0
#---Response level output have proportional with detection to the distance---
    while GPIO.input(echo_pin)==0: #wait for the echo pin turns high
        pulse_start=time.time() #record the time point before echo pin turns high
    while GPIO.input(echo_pin)==1: #wait for the echo pin turns low
        pulse_end=time.time() #record the time point before echo pin turns low
#-----------------------------------------------------------------------------
    t=pulse_end-pulse_start
    d=(t*v)/2
    return d*100

def detection_average():
    d1=detection()
    time.sleep(0.065)

    d2=detection()
    time.sleep(0.065)

    d3=detection()
    time.sleep(0.065)

    distance = (d1+d2+d3)/3
    return distance

def alarm(distance):
    if distance>50:
        warning=0
        pwm_buzzer.ChangeDutyCycle(0)
        time.sleep(0.6)
    elif distance<=50 and distance>20:
        warning=0
        pwm_buzzer.ChangeDutyCycle(0)
        pwm_buzzer.ChangeDutyCycle(50)
        time.sleep(0.3)
        pwm_buzzer.ChangeDutyCycle(0)
    elif distance<=20 and distance>2:
        pwm_buzzer.ChangeDutyCycle(50)

try:
    print 'Start...'
    for i in range (3):
        pwm_buzzer.ChangeDutyCycle(50)
        time.sleep(0.3)
    while True:
        for i in xrange(0,4,1):
            distance=detection_average()
            alarm(distance)
        print "Distance = %.1f cm\n" % distance

except KeyboardInterrupt:
    print "\nException: KeyboardInterrupt\n"

finally:
    pwm_buzzer.stop()
    GPIO.cleanup()
