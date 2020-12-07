import argparse
import configparser
import socket

parser = argparse.ArgumentParser(description='Sleep a computer on the LAN')
parser.add_argument('hostname', type=str, help='host to sleep')
args = parser.parse_args()

config = configparser.ConfigParser()
config.read('sleep.ini')

HOST = socket.gethostbyname(args.hostname)  # The server's hostname or IP address
PORT = int(config['sleeper']['port'])  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'sleep')  # send the sleep command
    response = s.recv(1024)
    if not response:
        print('ACK not received from target host')
    else:
        response = response.decode('ascii')
        print(response)
