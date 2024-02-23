import threading
import socket

host = '127.0.0.1'
port = 51531

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
User_Names = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index =  clients.index(client)
            clients.remove(client)
            client.close
            User_Name = User_Names[index]
            broadcast(f'(User_Name) left the chat'. encode('ascii'))
            User_Names.remove(User_Name)
            break

def receive():
    while True:
        client, address= server.accept()
        print(f'connected with {str(address)}')

        client.send('USER'. encode('ascii'))
        User_Name = client.recv(1024).decode('ascii')
        User_Names.append(User_Name)
        clients.append(client)

        print(f'User_Name of the client is {User_Name}')
        broadcast(f'{User_Name} joined the chat'.encode('ascii'))
        client.send('connected to the server'.encode('ascii'))

        thread = threading.Thread(target= handle, args=(clients,))
        thread.start()

print('waiting for connection...')
receive()