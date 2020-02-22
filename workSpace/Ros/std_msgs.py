'''
- Interface of all messages objects that uRos uses
- Default messages implemented are :
    - Empty message
    - string
    - number
    - point
    - Time TODO
'''
class Msg_I:
    
    def get_data(self):
        raise(Exception("Un impelemented, Inherit this class in your code"))
    
    @staticmethod
    def load_msg(string):
        '''
        Convert string json file to a message object
        :param string: json string representation
        :type string: String
        :return : return a message object
        :rtype : is determined by the subclass
        '''
        raise(Exception("Un impelemented, Inherit this class in your code"))

class std_Empty (Msg_I):
    def __init__(self):
        pass

    def get_data(self):
        dic = {
            "msg_type" : "Empty",
            "data" : {}
        }
        return dic
    
    @staticmethod
    def load_msg(data):
        return std_Empty()

class std_string (Msg_I):
    def __init__(self, string):
        self.string = string

    def get_data(self):
        dic = {
            "msg_type" : "String",
            "data" : {
                "string" : self.string
            }
        }
        return dic
    
    @staticmethod
    def load_msg(data):
        return std_string(data["string"])

class std_number (Msg_I):
    def __init__(self, number, numberType):
        self.number = number
        self.numberType = numberType

    def get_data(self):
        dic = {
            "msg_type" : "std_" + numberType,
            "data" : {
                "number" : self.number,
                "number_type" : self.numberType
            }
        }
        return dic
    
    @staticmethod
    def load_msg(data):
        return std_number(data["number"],data["numberType"])

class std_point (Msg_I):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_data(self):
        dic = {
            "msg_type" : "Point",
            "data" : {
                "x" : self.x,
                "y" : self.y,
                "z" : self.z
            }
        }
        return dic
    
    @staticmethod
    def load_msg(data):
        return std_point(data["x"], data["y"], data["z"])
