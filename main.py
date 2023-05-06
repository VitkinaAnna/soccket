import socket
import time

x = int(input("Введіть значення х: "))

def f(x):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5000))
        s.sendall(str(x).encode())
        result = s.recv(1024).decode()
        return int(result)

def g(x):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 6000))
        s.sendall(str(x).encode())
        result = s.recv(1024).decode()
        return int(result)

while True:
    result_f = None
    result_g = None
    try:
        result_f = f(x)
    except Exception as e:
        print(repr(e))

    try:
        result_g = g(x)
    except Exception as e:
        print(repr(e))

    if result_f is None or result_g is None:
        action = input("Ви хочете продовжити (1), зупинити (2), або продовжити не перепитуючи більше (3)? ")
        if action == "2":
            result = bool(result_f and result_g)
            print(f"f({x}) && g({x}) = {result}")
            break
        elif action == "3":
            continue
        else:
            print("Некоректне число. Продовження...")

    else:
        result = bool(result_f and result_g)
        print(f"f({x}) && g({x}) = {result}")
        break

time.sleep(1)
