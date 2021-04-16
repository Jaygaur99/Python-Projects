import socket
from select import select
from os import path
import time

IP_ADDRESS = 'localhost'
PORT = 12345
address = (IP_ADDRESS, PORT)
GET_CODE = "GETDATA"
FILE_TO_SEND = 'SEND/img.jpg'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen()
socket_list = [server_socket]
print(f"Listening for connections on {IP_ADDRESS}:{PORT}")
clients = {}
write_sockets = []

def receive_message(client_socket):
    data = client_socket.recv(1024).decode('utf8')
    if len(data) == 0:
        return False
    return data

try:
    while True:
        read_socket, write_socket, exception_sockets = select(socket_list, write_sockets, socket_list)
        for soc in read_socket:
            if soc == server_socket:
                client_socket, client_address = server_socket.accept()
                username = receive_message(client_socket)
                if username is False:
                    continue
                if username == GET_CODE:
                    write_sockets.append(client_socket)
                    print("write_sockets")
                    continue
                socket_list.append(client_socket)
                clients[client_socket] = username
                print("Accepted Connection from {0}:{1}, username: {2}".format(*client_address, username))
            else:
                message = receive_message(soc)
                if message == 'GETDATA':
                    break
                if message is False:
                    print("Closed continue from {}".format(clients[soc]))
                    soc.close()
                    socket_list.remove(soc)
                    del clients[soc]
                    continue
                username = clients[soc]
                print(f'Received message from {username}: {message}')
                for client in clients:
                    if client != soc:
                        client.send(f"{username} ---> {message}".encode('utf-8'))

        for soc in write_sockets:
            message = receive_message(soc)
            if message == GET_CODE:
                
                file = path.getsize(FILE_TO_SEND)
                file = bin(file)
                file = file.encode('utf-8')
                soc.send(file)
                print("Sending the file Now")
                with open(FILE_TO_SEND, 'rb') as f:
                    for i in f:
                        soc.send(i)
                    else:
                        print("file sent")
                continue
        for notified_socket in exception_sockets:
            socket_list.remove(notified_socket)
            del clients[notified_socket]
except Exception as e:
    server_socket.close()
    print("ERROR: {}".format(e))