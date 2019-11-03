import time

time1 = 0
time2 = 0
time3 = 0
state = 0
pwmValue = 0

def irqCallback(pin):
    global state,time1,time2,time3,pwmValue
    if state == 0:
        state = 1
        time1 = time.ticks_cpu()
        pin.irq(trigger=2,handler=irqCallback)
    elif state == 1 :
        state = 2
        time2 = time.ticks_cpu()
        pin.irq(trigger=1,handler=irqCallback)
    else :
        pin.irq(trigger=0,handler=irqCallback)
        state = 0
        time3 = time.ticks_cpu()
        pwmValue = int(((time2-time1)/(time3-time1))*1024)


def calcPWM(pin):
    global pwmValue
    pin.irq(trigger=1,handler=irqCallback)
    while(pwmValue == 0):
        pass
    temp = pwmValue
    pwmValue = 0
    return temp