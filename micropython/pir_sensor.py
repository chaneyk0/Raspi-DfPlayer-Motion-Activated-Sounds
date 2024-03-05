from machine import Pin
from time import sleep

PIR_sensor = Pin(18, Pin.IN, Pin.PULL_UP)

sleep(3)

while True:
   print(PIR_sensor.value())
   if PIR_sensor.value() == 0:
       print("No motion detected")
       sleep(2)
   else:
       print("Motion Detected!")
       sleep(5)