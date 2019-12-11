from machine import Pin
from pwmMesure import calcPWM
import time

a = Pin(2,Pin.IN)
sum = 0
r = 1
t1 = time.ticks_ms()
for c in range(r):
    sum += calcPWM(a)
print(sum/r)
print("time for 6 channels  is ",time.ticks_ms()*6-t1*6,"ms")