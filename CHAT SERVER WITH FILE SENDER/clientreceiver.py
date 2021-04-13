import socket
import select
from sys import exit
import errno
from time import sleep

IP_ADDRESS = 'localhost'
PORT = 12345
address = (IP_ADDRESS, PORT)
GET_CODE = "GETDATA"
RECEIVE_NAME_PATH ='RECEIVE/file.txt'


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

name = GET_CODE.encode('utf8')
client_socket.send(name)
print("Waiting to receive")
sleep(1)
msg = GET_CODE.encode('utf-8')
client_socket.send(msg)
file_size = int(client_socket.recv(1024), 2)
print("Now Receiving")
try:
    with open(RECEIVE_NAME_PATH,'w') as f:
        file = client_socket.recv(file_size).decode('utf-8')
        f.write(file)
except Exception as e:
    print("ERROR: " + str(e))
else:
    print("File Received successfully")

    