##New Device Template
##New Devices should be added into the initalState() function in
##the device mod which will add the new device to every device
import socket
import device ##mod with device class and other useful funcs
import select

##DEVICE
ThisDevice = device.device("device", "off")

##SOCKET
s = socket.socket()
host = socket.gethostname()
port = 7777

##Start State/Variables
deviceList = []
currentStateDict = device.initialState()
server_on = True

##COMMANDS: add new commands to the commandList as tupples
##(list of the requirements(tupples), action("on"/"off"))
##please be careful to not put mutually exclusive commands on
##the same device or commands on several devices that will result
##in oscillation. Commands at the end of the list will supercede
##previous commands if there is a contradiction
commandList = []



##Functions- handle incoming data and determines what to return

def makeStateList():
    stateList = []
    for each in currentStateDict.keys():
        stateList.append((each, currentStateDict[each]))
    return stateList

def handleData(data):
    if data == "SHUTDOWN":
        server_on = False
    else:
        x = device.strToTup(data)
        currentStateDict[x[0]] = x[1]
        if x[0] == ThisDevice.name:
            ThisDevice.status = x[1]
        else:
            changeTest = 0
            if device.commandType(data) == "A":
                for i in commandList:
                    var1 = True
                    stateList = makeStateList()
                    if x in i[0]:
                        for ii in i[0]:
                            if ii not in stateList:
                                var1 = False
                        if var1 == True:
                            ThisDevice.status = i[1]
                            changeTest += 1
                if changeTest < 0:
                    s.send(ThisDevice.state() + ' A')
                
            
            
            


s.connect((host, port))
while server_on:
    readable, writable, error = select.select([s],[s],[],5)
    if readable != []:
        data = s.recv(2048)
        handleData(data)

s.close()
    
