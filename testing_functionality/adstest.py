from ads1115 import ADS1115
from machine import I2C,Pin
import time

rate = 1
min = 32768
max = 0
def calcOffset(adsObject,channel):
    global min, max
    t1 = time.ticks_ms()
    sum = 0
    for a in range(50):
        reading = adsObject.read(rate,channel)
        if(reading > max) :
            max = reading
        if(reading < min):
            min = reading
        sum += reading
        time.sleep(0.03)
    print("time is ",(time.ticks_ms()-t1)/50," ms")
    return sum/50

i2c = I2C(scl = Pin(22), sda = Pin(21))
ADC0 = ADS1115(i2c, 72, 0)
#ADC1 = ADS1115(i2c, 73, 0)

offset = []
offset.append(calcOffset(ADC0,0))
offset.append(calcOffset(ADC0,1))
offset.append(calcOffset(ADC0,2))
offset.append(calcOffset(ADC0,3))
#offset.append(calcOffset(ADC1,0))
#offset.append(calcOffset(ADC1,1))
#offset.append(calcOffset(ADC1,2))
#offset.append(calcOffset(ADC1,3))
print("Error range is ",(max-min)*4.687643)

while (True):
    t1 = time.ticks_us()
    channel0  = ADC0.read(rate,0)
    channel1  = ADC0.read(rate,1)
    channel2  = ADC0.read(rate,2)
    channel3  = ADC0.read(rate,3)
    channel0  = ADC0.read(rate,0)
    channel1  = ADC0.read(rate,1)
    channel2  = ADC0.read(rate,2)
    channel3  = ADC0.read(rate,3)
    print((channel0-offset[0])*4.687643,"mA")
    print((channel1-offset[1])*4.687643,"mA")
    print((channel2-offset[2])*4.687643,"mA")
    print((channel3-offset[3])*4.687643,"mA")
    print((channel0-offset[0])*4.687643,"mA")
    print((channel1-offset[1])*4.687643,"mA")
    print((channel2-offset[2])*4.687643,"mA")
    print((channel3-offset[3])*4.687643,"mA")
    print("time is ",time.ticks_us()-t1," us")
    #1/32767*6.144*1000/40*1000
    #channel4  = ADC1.read(0,0)
    #channel5  = ADC1.read(0,1)
    #channel6  = ADC1.read(0,2)
    #channel7  = ADC1.read(0,3)
    #time.sleep()
    print("")
