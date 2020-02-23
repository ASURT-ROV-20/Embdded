from machine import Timer, Pin
import time

time1 = 0
time2 = 0
time3 = 0
state = 0
pwmValue = 0
skip = False
tim = Timer(-1)

pwmPin1 = Pin(14, Pin.IN)
pwmPin2 = Pin(14, Pin.IN)
pwmPin3 = Pin(14, Pin.IN)
pwmPin4 = Pin(14, Pin.IN)
pwmPin5 = Pin(14, Pin.IN)
pwmPin6 = Pin(14, Pin.IN)

_PWM_CHANNEL_1 = "CH1"
_PWM_CHANNEL_2 = "CH2"
_PWM_CHANNEL_3 = "CH3"
_PWM_CHANNEL_4 = "CH4"
_PWM_CHANNEL_5 = "CH5"
_PWM_CHANNEL_6 = "CH6"

def skipCallback(d):
    global skip, pwmValue
    skip = True
    pwmValue = -1

def irqCallback(pin):
    global state, time1, time2, time3, pwmValue
    if state == 0 and not(skip):
        state = 1
        time1 = time.ticks_cpu()
        pin.irq(trigger = Pin.IRQ_FALLING, handler=irqCallback)
    elif state == 1 and not(skip):
        state = 2
        time2 = time.ticks_cpu()
        pin.irq(trigger = Pin.IRQ_RISING, handler=irqCallback)
    elif not(skip):
        pin.irq(trigger = 0)
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
    pin.irq(trigger = Pin.IRQ_RISING, handler = irqCallback)
    tim.init(mode=Timer.ONE_SHOT, period=50, callback=skipCallback)
    while(pwmValue == 0 and not(skip)):
        pass
    tim.deinit()
    temp = pwmValue
    pwmValue = 0
    return temp

def pwmMesure():
    global pwmPin1, pwmPin2, pwmPin3, pwmPin4, pwmPin5, pwmPin6
    output = []
    output.append(calcPWM(pwmPin1))
    output.append(calcPWM(pwmPin2))
    output.append(calcPWM(pwmPin3))
    output.append(calcPWM(pwmPin4))
    output.append(calcPWM(pwmPin5))
    output.append(calcPWM(pwmPin6))
    return output