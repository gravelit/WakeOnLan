import socket
import configparser
import subprocess

config = configparser.ConfigParser()
config.read('sleep.ini')

HOST_NAME = socket.gethostname()  # Get the name of this machine
HOST = socket.gethostbyname(HOST_NAME)  # Run server on this machine
PORT = int(config['sleeper']['port'])  # Port to listen on (non-privileged ports are > 1023)

# Open a TCP listening socket with a IPv4 address
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()  # allows us to accept connections

    # Start listening for connections
    while True:
        conn, addr = s.accept()  # block and wait for client to connect, creates a new socket
        with conn:
            while True:
                data = conn.recv(1024)  # read what client sends
                if not data:
                    break
                command = data.decode('ascii')
                if command.lower() == 'sleep':
                    ack = ('Sleeping {}!'.format(HOST_NAME)).encode('ascii')
                    conn.sendall(ack)  # Acknowledge sleep request
                    subprocess.Popen(['sleep.bat'])
