
from gpiozero import DistanceSensor,Buzzer
from time import sleep

buzzer = Buzzer(3)
buzzer.on()
sensor = DistanceSensor(echo=18, trigger=17)
while True:
    distance = sensor.distance * 100   
    if(distance>20):
        buzzer.on()
    else:
        buzzer.off()
        buzzer.beep(0.1,0.1,None)
    print("Distance: ", distance)
    sleep(1)
