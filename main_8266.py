from gpio import gpio_8266 as gpio
from machine import Pin, PWM
from pwmMesure import calcPWM
import time

a = Pin(gpio("D3"), Pin.IN)
b = Pin(gpio("D4"), Pin.IN)
c = Pin(gpio("D5"), Pin.IN)
d = Pin(gpio("D6"), Pin.IN)
e = Pin(gpio("D7"), Pin.IN)
f = Pin(gpio("D8"), Pin.IN)
while(True):
    a_output = 0
    b_output = 0
    c_output = 0
    d_output = 0
    e_output = 0
    f_output = 0
    for count in range(5):
        a_output += calcPWM(a)
        b_output += calcPWM(b)
        c_output += calcPWM(c)
        d_output += calcPWM(d)
        e_output += calcPWM(e)
        f_output += calcPWM(f)
        time.sleep(0.01)
    print("First channel",a_output/5, " should be 200 error is ", ((a_output/5-200)/200)*100,"%")
    print("Second channel",b_output/5, "should be 233 error is ", ((b_output/5-233)/233)*100,"%")
    print("Third channel",c_output/5, "should be 266 error is ", ((c_output/5-266)/266)*100,"%")
    print("Fourth channel",d_output/5, "should be 299 error is ", ((d_output/5-299)/299)*100,"%")
    print("Fifth channel",e_output/5, "should be 332 error is ", ((e_output/5-332)/332)*100,"%")
    print("Sixth channel",f_output/5, "should be 365 error is ", ((f_output/5-365)/365)*100,"%")
    print("\n")
    time.sleep(3)