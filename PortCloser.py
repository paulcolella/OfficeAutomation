import socket
import time

s = socket.socket()
host = socket.gethostname()
port = 7777

s.connect((host, port))
s.close

