import gc
import network
import socket
import _thread
import esp
from time import sleep_ms
from server import setHandeler , serve, sendJson, run_server, set_resource_folder
from main import run_mesure, getJson

ip = ""
connected = False
station = network.WLAN(network.STA_IF)                                          
station.active(True)
print("Nodemcu .. Micropython iot board")
print("connecting to WIFI ...")
available = station.scan()
names = [name[0] for name in available]
print("avialabe ssids : ")
for name in names :
	print("\t" + str(name))
ssid = 'HOME-MCU'#input("ssid : ")
password = '1351968gamal21' #input("password : ")
station.connect(ssid,password)
ip = 0
for triels in range(50):
    sleep_ms(500)
    if station.isconnected() :
        ip = station.ifconfig()[0]
        print("Connected to " + ssid)
        print("connect your browser to ",ip+":80")
        connected = True
        break
    else :
        print("Trying to connect to " + ssid)

del available, names, ssid, password
gc.collect()

if(connected):
    setHandeler({"/" : [serve,"page.html"]})
    setHandeler({"reading" : [sendJson,getJson]})
    #set_resource_folder("webSite")
    _thread.start_new_thread(run_server, (80,))
    _thread.start_new_thread(run_mesure, ())