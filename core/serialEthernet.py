from machine import UART
from math import ceil
import _thread
from time import sleep

class SerialEthernet():
	def __init__(self, uartNumber, callback, bufferSize = 60):
		self.uart = UART(uartNumber)
		self.callback = callback
		self._listening = False
		self._sendBuffer = bufferSize

	def _listen(self):
		while True:
			if(self.uart.any()):
				self.callback(self.uart.readline())

	def start(self):
		_thread.start_new_thread(self._listen,[])

	def send(self, msg):
		trials = ceil(len(msg)/self.sendBuffer)
		for t in range(trials):
			self.uart.write(msg[a:a+59])
			sleep(0.1)