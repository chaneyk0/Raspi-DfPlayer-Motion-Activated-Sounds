from dfplayermini import Player
from machine import Pin
from time import sleep

# Initialize the DFPlayer Mini
sound = Player(pin_TX=Pin(0), pin_RX=Pin(1))

# Set the volume (adjust as needed)
sound.volume(10)

def play_sound():
    x = 1

    while x < 11:
        print("Playing track " + str(x))
        sound.play(x)
        sleep(30)  # Assuming each track plays for 2 minutes
        x += 1

    print('End of tracks')

# Initialize the PIR sensor
PIR_sensor = Pin(18, Pin.IN, Pin.PULL_UP)

while True:
    pir_value = PIR_sensor.value()
    print("PIR Sensor value:", pir_value)

    if pir_value == 0:
        print("No motion detected")
        sleep(1)  # Adjust as needed
    else:
       print("Motion Detected! Playing sound.")
       play_sound()
       sleep(30)

    sleep(1)  # Adjust the delay based on your application requirements
