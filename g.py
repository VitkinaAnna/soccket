import socket
import time

def g(x):
    g_x = x + 2
    return g_x

HOST = 'localhost'
PORT = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            x = int(data.decode())
            result = str(g(x))
            conn.sendall(result.encode())
    time.sleep(1)
