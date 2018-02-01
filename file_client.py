
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from pickle import dumps, loads


def file_client_hanlder(client):
    client = socket()
    client.connect(('127.0.0.1', 1234))
    file_name = input('Enter file name :')
    client.send(file_name.encode())
    file = loads(client.recv(1024))
    if file[0] == 200:
        f = open(client_root+'/'+file_name. 'wb')
        f.write(file[1])
        f.close()
        print('file downloaded')
    else:
        print('error 404 file not found')
