import time
from machine import Timer
time1 = 0
time2 = 0
time3 = 0
state = 0
pwmValue = 0
skip = False
tim = Timer(-1)

def skipCallback(d):
    global skip
    skip = True

def irqCallback(pin):
    global state,time1,time2,time3,pwmValue
    if state == 0 and not(skip):
        state = 1
        time1 = time.ticks_cpu()
        pin.irq(trigger=2,handler=irqCallback)
    elif state == 1 and not(skip):
        state = 2
        time2 = time.ticks_cpu()
        pin.irq(trigger=1,handler=irqCallback)
    elif not(skip):
        pin.irq(trigger=0,handler=irqCallback)
        state = 0
        time3 = time.ticks_cpu()
        pwmValue = int(((time2-time1)/(time3-time1))*4095) #255 for arduino, 4096 for hat


def calcPWM(pin):
    global pwmValue, time1, time2, time3, skip, tim
    time1 = 0
    time2 = 0
    time3 = 0
    state = 0
    pwmValue = 0
    skip = False
    pin.irq(trigger=1,handler=irqCallback)
    tim.init(mode=Timer.ONE_SHOT, period=50, callback=skipCallback)
    while(pwmValue == 0 and not(skip)):
        pass
    tim.deinit()
    temp = pwmValue
    pwmValue = 0
    return temp