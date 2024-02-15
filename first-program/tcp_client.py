"""
    Module that provides a client for server connection
"""
import socket

HOST = "127.0.0.1"
PORT = 65432

# AF_INET = IPV4, SOCK_STREAM = TCP Protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, server! This is client!")
    data = s.recv(1024)

print(f"Received from server: {data!r}")
