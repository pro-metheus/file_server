
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from pickle import dumps, loads

CLIENT_ROOT = '' #ENTER CLIENT DOWNLOADS FOLDER HERE

def file_client_hanlder(client):
    file_name = input('Enter file name :')
    client.send(file_name.encode())
    file = loads(client.recv(1024))
    if file[0] == 200:
        f = open(CLIENT_ROOT+'/'+file_name. 'wb')
        f.write(file[1])
        f.close()
        print('file downloaded')
    else:
        print('error 404 file not found')



if __name__ == '__main__':
client = socket()
client.connect(('127.0.0.1', 1234))
file_client_handler(client)
