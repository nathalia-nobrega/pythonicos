"""
    Module that provides a TCP Server
"""
import socket

HOST = "127.0.0.1"
PORT = 65432

# AF_INET = IPV4, SOCK_STREAM = TCP Protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Associate the scoket with a net interface and port
    s.bind((HOST, PORT))
    # Listens for new connections
    s.listen()
    # Accepts a new connection, returning a new socket obj and the addr of the client
    conn, addr = s.accept()
    # Reads whatever data the client sends and echoes it back
    with conn:
        print(f"Connect by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
