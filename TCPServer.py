from socket import *
from urllib import request

serverport = 12345 
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverport))
serverSocket.listen(2) 

print('server is ready to receive')

def service(socket):
    print(f'Connection established with {addr}')
    message = connectionSocket.recv(1024).decode()
    print(f'Received message: {message}')
    
    connectionSocket.send(message.encode())
    print(f'Sent back: {message}')
    connectionSocket.close()
    