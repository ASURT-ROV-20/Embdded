import _thread
import time

def testThread(message,period):
  while True:
    print("Hello from thread ",message)
    time.sleep(period)

def locThread():
    b = 0
    while True:
        a = 5
        b += 1
        if(b%1000 == 0):
            print("working")
    
  

_thread.start_new_thread(locThread, ())
_thread.start_new_thread(locThread, ())