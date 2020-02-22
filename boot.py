from core.sdcard import SDCard
from machine import SPI, Pin
import os

sd = SDCard(SPI(2 , sck = Pin(18), miso = Pin(19), mosi = Pin(23)), Pin(5))
os.mount(sd, '/sd')