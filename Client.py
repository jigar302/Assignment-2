# runs on Pi

import socket
s = socket.socket()
host = '10.102.13.67'
port = 5000
s.connect((host, port))
print(s.recv(1024))
s.close()