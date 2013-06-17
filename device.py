##device
##status(on/off)
from string import *

class device():
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def state():
        return self.name + ' ' + self.status

def strToTup(string):
    if " " in string:
        x = string.split(" ")
        return (x[0], x[1])

def commandType(string):
    x = string.split(" ")
    if len(x) > 2:
        return x[2]
        
def initialState():
    return {"device1": "off","device2": "off","device3": "off"}
