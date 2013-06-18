import socket
import select

## socket: s.setsockopt IMPORTANT. Without this if the program is killed
##the same port will not be usable until a program is run which closes
##the port a simple program to close ports which have been left open is
##in the same file as this server named PortCloser.py
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 7776
s.bind((host, port))

##Variables
RcList = [s]    ##Readable Connection List
WcList = []     ##Writeable Connection List
UserList = []
server_on = True


##Functions

def removeConnection(connection):
    RcList.remove(connection)
    WcList.remove(connection)
    
        
##Server Operation: this will bounce the data as it is sent in
##to all the connected devices
s.listen(5)
while server_on:
    readable, writable, errored = select.select(RcList, WcList,[],10)
    if s in readable:
        client_socket, address = s.accept()
        print "Connection from", address
        RcList.append(client_socket)
        WcList.append(client_socket)
        readable.remove(s)
    for i in readable:
        data = i.recv(2048)
        if data == "User":
            removeConnection(i)
            readable.remove(i)
            writable.remove(i)
            i.close()
            print str(i) + " removed"
        else:
            print data
            if data == "SHUTDOWN":
                server_on = False
            for ii in writable:
                    ii.send(data)

s.close()

