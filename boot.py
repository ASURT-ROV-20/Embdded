# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
from main import *
#import webrepl
#webrepl.start()
gc.collect()
init()
start()
