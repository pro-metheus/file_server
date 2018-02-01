'''
simple fileserver written in python
'''

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from pickle import dumps, loads
import os


def file_server_hanlder(client):
    '''
    basically just sends the byte stream of file content
    '''
    file_name = client.recv(1024).decode()
    contents = os.listdir(settings.SERVER_ROOT)
    found = 0
    for content in contents:
        if file_name == content:
            f = open(settings.SERVER_ROOT+'/'+file_name, 'rb')
            file_content = f.read()
            package = []
            package[0] = 200
            package[1] = file_content
            client.send(dumps(package))
            found = 1
            break
        else:
            found = 0
    if found == 0:
        package = [404, 'file not found']
        client.send(dumps(package))


if __name__ == '__main__':
    server = socket()
    server.bind(('127.0.0.1', 1234))
    server.listen(5)
    while True:
        client, addr = server.accept()
        t = Thread(target=file_server, args=(client,))
        t.start()
        
