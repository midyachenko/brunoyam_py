import socket, threading

HOST='localhost'
#HOST='aud21-prep'

PORT=12356

def receive_data(sock):
    while True:
        data=sock.recv(1024)
        print(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    while True:
        user_input=input()
        client.sendall(bytes(user_input.encode('utf-8')))

        #data=client.recv(1024)
        #print(data)