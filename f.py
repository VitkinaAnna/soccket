import socket
import time

def f(x):
    f_x = x//x
    return f_x

HOST = 'localhost'
PORT = 5000

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
            result = str(f(x))
            conn.sendall(result.encode())
    time.sleep(1)  #Чекати 1 секунду
