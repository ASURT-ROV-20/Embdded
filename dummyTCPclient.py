import socket
import time
import json

a = {
	"Time": [2000, 1, 1, 5, 1, 12, 54, 72591],
	"ADC": [0,0,0,0,0,0,0,0],
	"PWM": [0,0,0,0,0,0]
}

b = {
	"Time": [2000, 1, 1, 5, 1, 12, 54, 72591],
	"ADC": [0,0,0,0,0,0,0,0],
	"PWM": [0,0,0,0,0,0]
}


c = {
	"Time": [2000, 1, 1, 5, 1, 12, 54, 72591],
	"ADC": [0,0,0,0,0,0,0,0],
	"PWM": [0,0,0,0,0,0]
}


b = [json.dumps(a),json.dumps(b),json.dumps(c)]

soc = socket.socket()
soc.connect(("127.0.0.1",8000))
while True:
	soc.send(json.dumps(a).encode())
	print(json.dumps(a))
	time.sleep(1)

