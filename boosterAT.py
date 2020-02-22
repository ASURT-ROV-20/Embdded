from machine import UART
import time

serial = UART(2)

def printSerial():
	global serial
	while not(serial.any()) :
		pass
	print(str(serial.read()))



serial.write("AT+RST\r\n")
time.sleep(5)
printSerial()
serial.write("AT+CWMODE=1\r\n")
printSerial()
serial.write("AT+CWMODE?\r\n")
printSerial()
serial.write("AT+CWLAP\r\n")
time.sleep(5)
printSerial()
serial.write("AT+CWJAP=\"MGTM\",\"81119988111998\"\r\n")
time.sleep(5)
printSerial()
serial.write("AT+CIFSR\r\n")
time.sleep(5)
printSerial()
