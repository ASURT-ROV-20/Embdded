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
        self._ip = None
        self._port = None
        self.send("AT+START")
        sleep(5)

    def _listen(self):
        while True:
            if(self.uart.any()):
                self.callback(self.uart.readline())

    def setIP(self, ip, port):
        self._ip = ip
        self._port = port
        self.send("AT+CONNECT")
        self.send(str(ip[0]))
        self.send(str(ip[1]))
        self.send(str(ip[2]))
        self.send(str(ip[3]))
        self.send(str(port))
        self.send("AT+SEND")

    def start(self):
        _thread.start_new_thread(self._listen,[])

    def send(self, msg):
        trials = ceil(len(msg)/self._sendBuffer)
        for t in range(trials):
            #print("t : ", t)
            #print(msg[t*(self._sendBuffer-1):(t+1)*(self._sendBuffer-1)])
            self.uart.write(msg[t*(self._sendBuffer-1):(t+1)*(self._sendBuffer-1)])
            sleep(0.2)
        self.uart.write("\r")