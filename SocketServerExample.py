
import socket
server = socket.socket()
server.bind(('localhost', 50000))
server.listen()
server.accept()
s, addr = server.accept() #wait client connect
while 1:
    data = s.recv(1024)
    if not data:
        break
    s.sendall(data)
   
server.close()


'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
'''

