from core.adcMesure import adcMesure, init_ADC
from core.pwmMesure import pwmMesure
from core.serialEthernet import SerialEthernet
from machine import RTC
import ujson as json
import gc
import time

realTime = RTC()
# init_ADC()
ether = SerialEthernet(2,None)
ether.send("System Started")

while(True):
    data = {}
    data["Time"] = realTime.datetime()
    data["PWM"]  = pwmMesure()
    data["ADC"]  = adcMesure()
    data = json.dumps(data)
    log = open("sd/log1.txt", 'a')
    log.write(data)
    log.write('\n')
    log.close()
    print(data[0:59])
    ether.send()
    gc.collect()
    print("LOG IS WRITTEN", gc.mem_free())
    time.sleep(2)
    
