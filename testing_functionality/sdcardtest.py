from machine import Pin
import machine
import sdcard
import os

sd = sdcard.SDCard(machine.SPI(2 , sck = Pin(18), miso = Pin(19), mosi = Pin(23)), Pin(5))
os.mount(sd, '/sd')

f = open('/sd/test2.txt','w')

for _ in range(500):
    f.write("Mohamed gamal \n")

f.close()