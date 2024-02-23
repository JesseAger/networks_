import threading
import socket
User_Name = input('Choose a User_Name:')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 51531))

def receive():
    while True:
        try:
            message = client.recv(1024)
            if message == 'USER':
                client.send(User_Name.encode('ascii'))
            else:
                print(message)
        except:
            print('An error ocurred')
            client.close()
            break

def write():
    while True:
        message = f'{User_Name}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()