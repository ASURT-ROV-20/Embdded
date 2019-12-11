from ads1115 import ADS1115
from machine import I2C,Pin
from pwmMesure import calcPWM
import time

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

def init():
    offset = []
    offset.append(calcOffset(ADC0,0))
    offset.append(calcOffset(ADC0,1))
    offset.append(calcOffset(ADC0,2))
    offset.append(calcOffset(ADC0,3))
    offset.append(calcOffset(ADC1,0))
    offset.append(calcOffset(ADC1,1))
    offset.append(calcOffset(ADC1,2))
    offset.append(calcOffset(ADC1,3))
    print("Error range in Current Mesurments is ",(max-min)*4.687643)
    return offset


def startMesurement():
    global offset, ADC0, ADC1, PWM
    while (True):
        #print(offset)
        t1 = time.ticks_ms()
        print("ADC Channel1 ",(ADC0.read(rate,0)-offset[0])*4.687643,"mA")
        print("ADC Channel2 ",(ADC0.read(rate,1)-offset[1])*4.687643,"mA")
        print("ADC Channel3 ",(ADC0.read(rate,2)-offset[2])*4.687643,"mA")
        print("ADC Channel4 ",(ADC0.read(rate,3)-offset[3])*4.687643,"mA")
        print("ADC Channel5 ",(ADC1.read(rate,0)-offset[0])*4.687643,"mA")
        print("ADC Channel6 ",(ADC1.read(rate,1)-offset[1])*4.687643,"mA")
        print("ADC Channel7 ",(ADC1.read(rate,2)-offset[2])*4.687643,"mA")
        print("ADC Channel8 ",(ADC1.read(rate,3)-offset[3])*4.687643,"mA")
        print("PWM Channel1 ",calcPWM(PWM[0]))
        print("PWM Channel2 ",calcPWM(PWM[1]))
        print("PWM Channel3 ",calcPWM(PWM[2]))
        print("PWM Channel4 ",calcPWM(PWM[3]))
        print("PWM Channel5 ",calcPWM(PWM[4]))
        print("PWM Channel6 ",calcPWM(PWM[5]))
        print("time is ",time.ticks_ms()-t1," ms")

rate = 1
min = 32768
max = 0
i2c = I2C(scl = Pin(22), sda = Pin(21))
ADC0 = ADS1115(i2c, 72, 0)
ADC1 = ADS1115(i2c, 73, 0)
pwm1 = Pin(2,Pin.IN)
pwm2 = Pin(2,Pin.IN)
pwm3 = Pin(2,Pin.IN)
pwm4 = Pin(2,Pin.IN)
pwm5 = Pin(2,Pin.IN)
pwm6 = Pin(2,Pin.IN)
offset = []
PWM = [pwm1, pwm2, pwm3, pwm4, pwm5, pwm6]


def run_mesure():
    global offset
    offset = init()
    startMesurement()
    
def getJson():
    return "json File"