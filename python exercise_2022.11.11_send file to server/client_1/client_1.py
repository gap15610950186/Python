import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',4444))
filename = 'C:/Users/B210/Desktop/python exercise_2022.11.11/client_1/send.txt'
print('I want to send a file to server')
s.send(filename.encode('utf-8'))
str1 = s.recv(1024)
str2 = str1.decode('utf-8')
if str2=='no':
    print('The server is rejects it')
else:
    s.recv(1024)
    size = 1024
    print('The server is accept the request')
    if os.path.exists(filename):
        with open(filename,'rb') as f:
            while True:
                data = f.read(size)
                s.send(data)
                if len(data) < size:
                    break
        print('send successfully')