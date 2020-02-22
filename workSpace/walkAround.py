import gc
import network
from time import sleep_ms
from machine import Pin

gc.collect()
station = network.WLAN(network.STA_IF)                                          
station.active(True)
print("Nodemcu .. Micropython iot board")
print("connecting to WIFI ...")
available = station.scan()
names = [name[0] for name in available]
print("avialabe ssids : ")
for name in names :
	print("\t" + str(name))
ssid = "HOME-MCU"#input("ssid : ")
password =  "1351968gamal21"#input("password : ")
station.connect(ssid,password)
ip = 0
for triels in range(15):
	sleep_ms(100)
	if station.isconnected() :
		ip = station.ifconfig()[0]
		print("Connected to " + ssid)
		break
	else :
		print("Trying to connect to " + ssid)
del available, names, ssid, password
