from Ros import *
try:
    import json
except ImportError:
    import ujson as json

ros = uRos(4)
ros.subscribe("testTopic",lambda msg : print(msg), std_Empty)
ros.subscribe("testTopic",lambda msg : print("Message from here : "), std_Empty)
empty = std_point(5,7,6)
a = ros.publish("testTopic",empty)
a = json.loads(a)
a["op"] = "topic_message"
print(a)
ros.test(a)
# dic = json.loads(a)
# print(dic)
# b = std_point.load_msg(dic["msg"]["data"])
# print(b)