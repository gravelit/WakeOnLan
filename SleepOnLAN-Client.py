import socket
import configparser

config = configparser.ConfigParser()
config.read('sleep.ini')

HOST = config['sleeper']['host']  # The server's hostname or IP address
PORT = config['sleeper']['port']  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))