from core.adcMesure import adcMesure, init_ADC
from core.pwmMesure import pwmMesure
from core.serialEthernet import SerialEthernet
from machine import RTC, Timer
import ujson as json
import gc
import time
import _thread

dataQueue = []
timer = Timer(0)

def onRead(msg):
    print(msg)

def sendData(_):
    global dataQueue
    print("Sending , queue size is",len(dataQueue))
    if len(dataQueue) == 0:
        timer.deinit()
        return
    data = dataQueue.pop(0)
    ether.send(data)
    #time.sleep(1)

def timerThread():
    timer.init(period=2000, mode=Timer.PERIODIC, callback=sendData)

realTime = RTC()
# init_ADC()
time.sleep(5)
ether = SerialEthernet(2,onRead,256)
ether.setIP((192, 168, 1, 109), 5000)
#ether.start()
_thread.start_new_thread(timerThread ,[])

while(True):
    data = {}
    data["Time"] = realTime.datetime()[1:7]
    data["PWM"]  = pwmMesure()
    data["ADC"]  = adcMesure()    
    data = json.dumps(data)
    data = data.replace(" ", "")
    log = open("sd/log1.txt", 'a')
    log.write(data)
    log.write('\n')
    log.close()
    data = data + "#\0"
    if(len(dataQueue) > 5):
        print("Removing from queue")
        dataQueue.pop(0)
    dataQueue.append(data)
    gc.collect()
    print("LOG IS WRITTEN", gc.mem_free())
    time.sleep(1)
    
