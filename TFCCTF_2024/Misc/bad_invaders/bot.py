import socket
import time

IP = "127.0.0.1"
PORT = 1337
addr = (IP, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)

s.settimeout(1.0)

s.send(b"N|bot;")

LAST_PING_TIME = time.time()
PLAYER_ID = -1

while True:
    if time.time() - LAST_PING_TIME > 2 and PLAYER_ID != -1:
        s.send(f"{PLAYER_ID}|P;".encode())
        LAST_PING_TIME = time.time()

    try:
        data = b""
        while True:
            new_data = s.recv(1)
            if new_data == b";":
                break
            data += new_data
    except socket.timeout:
        continue

    if not data:
        continue

    if data[:1] == b"J":
        PLAYER_ID = int(data[2:])

    if data[:1] == b"F":
        time.sleep(1)
        s.send(f"{PLAYER_ID}|M|1;".encode())
        time.sleep(2)
        s.send(f"{PLAYER_ID}|M|1;".encode())
        time.sleep(3)
        s.send(f"{PLAYER_ID}|M|1;".encode())
    