from machine import Pin,PWM,ADC,UART
from gpio import gpio_32
from pwmMesure import calcPWM
from time import time

def init():
    print("initalizing pins ...")
    #initalizing input pins to mesure pwms
    right_front_esc = Pin(gpio_32("D4"),Pin.IN)
    left_front_esc = Pin(gpio_32("D4"),Pin.IN)
    right_back_esc = Pin(gpio_32("D4"),Pin.IN)
    left_back_esc = Pin(gpio_32("D4"),Pin.IN)
    vertical_right_esc = Pin(gpio_32("D4"),Pin.IN)
    vertical_left_esc = Pin(gpio_32("D4"),Pin.IN)
    #initalizing ADC Pins 
    right_front_voltage = ADC(Pin(gpio_32("D4")))
    left_front_voltage = ADC(Pin(gpio_32("D4")))
    right_back_voltage = ADC(Pin(gpio_32("D4")))
    left_back_voltage = ADC(Pin(gpio_32("D4")))
    vertical_right_voltage = ADC(Pin(gpio_32("D4")))
    vertical_left_voltage = ADC(Pin(gpio_32("D4")))
    #Set attenuation fpr -11DB to mesure voltages from 0 to 3.3V
    right_front_voltage.atten(ADC.ATTN_11DB)
    left_front_voltage.atten(ADC.ATTN_11DB)
    right_back_voltage.atten(ADC.ATTN_11DB)
    left_back_voltage.atten(ADC.ATTN_11DB)
    vertical_right_voltage.atten(ADC.ATTN_11DB)
    vertical_left_voltage.atten(ADC.ATTN_11DB)
    #initialize uart
    uart = UART(0, baudrate=9600)
    

int start():
    while(1):
        print("right_front_esc : ",calcPWM(right_front_esc))
        uart.write(calcPWM(right_front_esc))
        print("left_front_esc : ",calcPWM(left_front_esc))
        uart.write(calcPWM(left_front_esc))
        print("right_back_esc : ",calcPWM(right_back_esc))
        uart.write(calcPWM(right_back_esc))
        print("left_back_esc : ",calcPWM(left_back_esc))
        uart.write(calcPWM(left_back_esc))
        print("vertical_right_esc : ",calcPWM(vertical_right_esc))
        uart.write(calcPWM(vertical_right_esc))
        print("vertical_left_esc : ",calcPWM(vertical_left_esc))
        uart.write(calcPWM(vertical_left_esc))
        
        print("right_front_voltage : ",right_front_voltage.read())
        uart.write(right_front_voltage.read())
        print("left_front_voltage : ",left_front_voltage.read())
        uart.write(left_front_voltage.read())
        print("right_back_voltage : ",right_back_voltage.read())
        uart.write(right_back_voltage.read())
        print("left_back_voltage : ",left_back_voltage.read())
        uart.write(left_back_voltage.read())
        print("vertical_right_voltage : ",vertical_right_voltage.read())
        uart.write(vertical_right_voltage.read())
        print("vertical_left_voltage : ",vertical_left_voltage.read())
        uart.write(vertical_left_voltage.read())
        time.sleep(1)
