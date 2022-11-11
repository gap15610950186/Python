import socket
import os
def recefile(conn):
    str1 = conn.recv(1024)
    filename = str1.decode('utf-8')
    print('The client requests send a file to me')
    result=str(input('agree or not:'))
    if result=='agree':
        print('I agree to accept it') 
        conn.send(b'yes')
        conn.send(b'I am ready!')
        temp=filename.split('/')
        myname = 'my_' + temp[len(temp)-1]
        size=1024
        with open(myname,'wb') as f:
            while True:
                data = conn.recv(size)
                f.write(data)
                if len(data)<size:
                    break
        print('The file is received successfully!')
    else:
        print('Sorry, I have no disagree to accept it')
        conn.send(b'no')
    conn.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',4444))
s.listen(1)
print('Waiting for connecting...')
while True:
   (conn,addr)=s.accept()
   recefile(conn)