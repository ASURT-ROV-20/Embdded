from core.adcMesure import adcMesure, init_ADC
from core.pwmMesure import pwmMesure
from machine import RTC
import ujson as json
import gc
import time

realTime = RTC()
# init_ADC()

while(True):
    data = {}
    data["Time"] = realTime.datetime()
    data["PWM"]  = pwmMesure()
    data["ADC"]  = adcMesure()
    log = open("sd/log1.txt", 'a')
    log.write(json.dumps(data))
    log.write('\n')
    log.close()
    gc.collect()
    print("LOG IS WRITTEN", gc.mem_free())
    
