
import socket

HOST = ''      # Listen on all interfaces
PORT = 65432   # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for a connection…")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received:", data.decode())
            conn.sendall(b"Message received")












client.py:

import socket

HOST = '192.168.1.100'  # Server Pi’s IP
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello from Client Pi")
    data = s.recv(1024)
    print("Server Response:", data.decode())
















sudo apt update && sudo apt upgrade -y

hostname -I
