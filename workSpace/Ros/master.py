from .std_msgs import std_Empty, std_number, std_point, std_string
from sys import platform as platform

if platform == "esp32":
    import ujson as json
    from machine import Timer
else :
    import json
    import threading
    



# Ros implementtation for micropython
# Hardware used is ESP32 & serial ethernet module
# Serial ethernet module is : atmega328 & enc28j60
# To use it with onther ethernet modules change ether attribute

class Ros :
    def __init__ (self, uartEther):
        self.ether = uartEther
        self.topic_subs = {}
        self.messagesType = [std_Empty, std_string, std_number, std_point]
        if platform == "esp32":
            self.timer = Timer(-1)
    
    def publish(self, topic_name, msg):
        data = {
            "op" : "topic_publish",
            "topic_name" : topic_name,
            "msg" : msg.get_data()
        }
        data_str = json.dumps(data)
        return data_str
        # self.ether.write(data_str)

    def subscribe(self, topic_name, callback, msgClass):
        if topic_name in self.topic_subs :
            if not(callback in self.topic_subs[topic_name]) :
                self.topic_subs[topic_name].append(callback)
        else:
            self.topic_subs[topic_name] = [callback]

        data = {
            "op" : "topic_subscibe",
            "topic_name" : topic_name,
            "msg_type" : msgClass.__name__,
        }
        data_str = json.dumps(data)
        # self.ether.write(data_str)

    def registerMassege(self, messageClass):
        if not(messageClass in self.messagesType):
            self.messagesType.append(messageClass)

    def __handel(self, dic):
        if dic["op"] == "topic_message":
            self.__topic_sub_handeler(dic)

    def __topic_sub_handeler(self, dic):
        print(self.topic_subs)
        callbackList = self.topic_subs[dic["topic_name"]]
        msg = dic["msg"]
        for classMsg in self.messagesType:
            if msg["msg_type"] == classMsg.__name__ :
                msgObj = classMsg.load_msg(msg["data"])
                for callBack in callbackList:
                    callBack(msgObj)
                return
        raise Exception("This message type is not Registered ...")

    def check(self):
        if(ether.any() > 0):
            inData = ether.read()
            dic = json.loads(inData)
            self.__handel(dic)
    
    def start(self):
        self.timer.init(mode=Timer.PERIODIC, period=250, callback=self.check)

    def test(self, dic):
        self.__handel(dic)