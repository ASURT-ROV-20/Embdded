from machine import UART

uart = UART(2)

while(True):
	if uart.any():
		print(uart.readline())