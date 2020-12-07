import socket
import configparser

config = configparser.ConfigParser()
config.read('sleep.ini')

HOST = config['sleeper']['host']  # Standard loopback interface address (localhost)
PORT = config['sleeper']['port']  # Port to listen on (non-privileged ports are > 1023)

# Open a TCP listening socket with a IPv4 address
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()  # allows us to accept connections
    #while True:
    conn, addr = s.accept()  # block and wait for client to connect, creates a new socket
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)  # read what client sends
            if not data:
                break
            print(data)
            conn.sendall(data)  # echo data back