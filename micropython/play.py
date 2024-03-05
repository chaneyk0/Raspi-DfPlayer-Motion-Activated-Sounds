from dfplayermini import Player
from machine import Pin, SPI
from time import sleep

sound = Player(pin_TX=Pin(0), pin_RX=Pin(1))

x=1
print("play sound")
sound.play(x)