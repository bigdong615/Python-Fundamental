
import socket
server = socket.socket()
server.connect(('localhost', 50000))
server.send('{}'.format('hello, world').encode())
data =server.recv(1024)
print('Received', repr(data))


'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
s.sendall('{}'.format('Hello, world').encode())
data = s.recv(1024)
s.close()
print ('Received', repr(data))
'''