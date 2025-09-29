from socket import *
from urllib import request

serverport = 54321
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverport))
serverSocket.listen(3) 

print('server is ready to receive')

def service(socket):
    print(f'Connection established with {addr}')
    message = socket.recv(1024).decode()
    print(f'Received message: {message}')

    socket.send(message.encode())
    print(f'Sent back: {message}')
    socket.close()


def random(socket):
    socket.send(f'Input two numbers between 1 and 10: \n'.encode())

    numbers = socket.recv(1024).decode().split()
    print(f'Received numbers: {numbers}')
    num1, num2 = int(numbers[0]), int(numbers[1])
    if 1 <= num1 <= 10 and 1 <= num2 <= 10:
        import random
        rand_num = random.randint(num1, num2)
        socket.send(f'Random number between {num1} and {num2}: {rand_num}\n'.encode())
    else:
        socket.send(f'Error: Numbers must be between 1 and 10.\n'.encode())



def add(socket):
    socket.send(f'Input two numbers between 1 and 10: \n'.encode())

    numbers = socket.recv(1024).decode().split()
    print(f'Received numbers: {numbers}')
    num1, num2 = int(numbers[0]), int(numbers[1])
    if 1 <= num1 <= 10 and 1 <= num2 <= 10:
        result = num1 + num2
        socket.send(f'Sum of {num1} and {num2}: {result}\n'.encode())
    else:
        socket.send(f'Error: Numbers must be between 1 and 10.\n'.encode())



def subtract(socket):
    socket.send(f'Input two numbers between 1 and 10: \n'.encode())

    numbers = socket.recv(1024).decode().split()
    print(f'Received numbers: {numbers}')
    num1, num2 = int(numbers[0]), int(numbers[1])
    if 1 <= num1 <= 10 and 1 <= num2 <= 10:
        result = num1 - num2
        socket.send(f'Subtraction of {num1} and {num2}: {result}\n'.encode())
    else:
        socket.send(f'Error: Numbers must be between 1 and 10.\n'.encode())





def convo(socket):
    socket.send(f'Choose an option: \n 1. random \n 2. add \n 3. subtract \n 4. exit'.encode())
    while True:
        request = socket.recv(1024).decode().strip()
        print(f'Received request: {request}')

        if request: 
            if request == 'random':
                random(socket)

            if request == 'add':
                    add(socket)

            if request == 'subtract':
                subtract(socket)
                
            if request == 'exit':
                socket.send(f'Goodbye!'.encode())
                print(f'Connection closed with {addr}')
                connectionSocket.close()
                break


    
# Alting køre pga. nedenstående linje 
connectionSocket, addr = serverSocket.accept()
# service(connectionSocket)
convo(connectionSocket)