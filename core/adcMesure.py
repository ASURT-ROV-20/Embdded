from .ads1115 import ADS1115 as ADC
from machine import I2C, Pin
import time

_ADC_SAMPLE_RATE = const(1)
_ADC_MIN_VALUE   = const(32768)
_ADC_MAX_VALUE   = const(0)

_ADC_CHANNEL_1   = "CH1"
_ADC_CHANNEL_2   = "CH2"
_ADC_CHANNEL_3   = "CH3"
_ADC_CHANNEL_4   = "CH4"
_ADC_CHANNEL_5   = "CH5"
_ADC_CHANNEL_6   = "CH6"
_ADC_CHANNEL_7   = "CH7"
_ADC_CHANNEL_8   = "CH8"

i2c = I2C(scl = Pin(22), sda = Pin(21))
adc0 = ADC(i2c, 72, 0)
adc1 = ADC(i2c, 73, 0)
offset = []

def calcOffset(adsObject,channel):
    max = _ADC_MIN_VALUE
    min = _ADC_MAX_VALUE
    sum = 0
    for a in range(50):
        reading = adsObject.read(_ADC_SAMPLE_RATE,channel)
        if(reading > max) :
            max = reading
        if(reading < min):
            min = reading
        sum += reading
        time.sleep(0.03)
    return sum/50

def init_ADC():
    global offset, adc0, adc1
    offset.append(calcOffset(adc0,0))
    offset.append(calcOffset(adc0,1))
    offset.append(calcOffset(adc0,2))
    offset.append(calcOffset(adc0,3))
    offset.append(calcOffset(adc1,0))
    offset.append(calcOffset(adc1,1))
    offset.append(calcOffset(adc1,2))
    offset.append(calcOffset(adc1,3))

def adcMesure():
    global adc0, adc1, offset
    output = []
    # output[_ADC_CHANNEL_1] = (adc0.read(_ADC_SAMPLE_RATE,0)-offset[0])
    # output[_ADC_CHANNEL_2] = (adc0.read(_ADC_SAMPLE_RATE,1)-offset[1])
    # output[_ADC_CHANNEL_3] = (adc0.read(_ADC_SAMPLE_RATE,2)-offset[2])
    # output[_ADC_CHANNEL_4] = (adc0.read(_ADC_SAMPLE_RATE,3)-offset[3])
    # output[_ADC_CHANNEL_5] = (adc1.read(_ADC_SAMPLE_RATE,0)-offset[4])
    # output[_ADC_CHANNEL_6] = (adc1.read(_ADC_SAMPLE_RATE,1)-offset[5])
    # output[_ADC_CHANNEL_7] = (adc1.read(_ADC_SAMPLE_RATE,2)-offset[6])
    # output[_ADC_CHANNEL_8] = (adc1.read(_ADC_SAMPLE_RATE,3)-offset[7])
    output.append(-1)
    output.append(-1)
    output.append(-1)
    output.append(-1)
    output.append(-1)
    output.append(-1)
    output.append(-1)
    output.append(-1)
    # time.sleep(0.8)
    return output
