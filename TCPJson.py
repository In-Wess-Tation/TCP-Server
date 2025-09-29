from socket import *
from urllib import request
import json
import threading
import random

serverport = 12345
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverport))
serverSocket.listen(3) 

print(f'server is ready to receive')

def service (connectionSocket):
    connectionSocket.send(json.dumps(f'Write a command and two seberate numbers. \n').encode())
    #{"command": "Random", "tal1": 1, "tal2": 9}
    #{"command": "Add", "tal1": 5, "tal2": 5}
    #{"command": "Subtract", "tal1": 10, "tal2": 8}
    #{"command": "Exit"}

    while True:
        data = connectionSocket.recv(1024).decode().strip()
        print(f"Received data: {data}")
        if not data:
            break
        try:
            req = json.loads(data)
  
            print(f"Parsed JSON: {req}")
            command = req.get("command")
            tal1 = req.get("tal1")
            tal2 = req.get("tal2")

            if command == "Exit":
                break  
            command = command.lower().capitalize()
            if command == "Random":
                    response = random.randint(int(tal1), int(tal2))
            elif command == "Add":
                    response = int(tal1) + int(tal2)
            elif command == "Subtract":
                    response = int(tal1) - int(tal2)
            else:
                    response = f"Error: Unknown command: {command}"

            connectionSocket.send(json.dumps({"response":response}).encode())
        except json.JSONDecodeError:
            connectionSocket.send(json.dumps({"error": "Invalid JSON"}).encode())
            break
    connectionSocket.close()
    

while True:
   connectionSocket,adr = serverSocket.accept()
   '''service(connectionSocket)'''

   threading.Thread(target=service, args=(connectionSocket,)).start()