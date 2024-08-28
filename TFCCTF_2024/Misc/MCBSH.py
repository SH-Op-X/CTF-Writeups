from pwn import *

white_chars = []
i = 32
while i < 127:
    conn = remote("challs.tfcctf.com", 30687)
    conn.recvuntil(b"root@????????$ ")
    while True:
        conn.sendline(chr(i))
        conn.recvline()
        s = conn.recvline()
        if b"[ERROR] Malicious input detected!" in s:
            break
        white_chars.append(chr(i))
        i += 1
    conn.close()
    print(white_chars)
    i += 1
