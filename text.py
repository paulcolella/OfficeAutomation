import socket
import time

s = socket.socket()
host = socket.gethostname()
port = 7778

s.connect((host, port))
time.sleep(5)
s.send("device3 on M")
print s.recv(2048)
print s.recv(2048)
print s.recv(2048)
s.close()
