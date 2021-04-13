import socket
import select
from sys import exit
import errno

IP_ADDRESS = 'localhost'
PORT = 12345
address = (IP_ADDRESS, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)
client_socket.setblocking(0)

name = input("Enter Username: ").encode('utf8')
client_socket.send(name)
is_on = True
while is_on:
    message = input("Message: ")
    if message == "STOP":
        is_on = False
    if message:
        message = message.encode('utf-8')
        client_socket.send(message)
    try:
        while True:
            user_msg = client_socket.recv(1024).decode('utf8')
            print(user_msg)
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            exit()
        continue
    except Exception as e:
        print('Reading error: '.format(str(e)))
        exit()

client_socket.close()
