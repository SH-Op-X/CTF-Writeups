from pwn import *
conn = remote('34.31.47.112', 31293)
for i in range(100):
    c = conn.recvuntil(b'submit test words > ')
    print(c.decode())
    s = c.decode().split()[3]
    # print(conn.recvline().decode())
    conn.sendline(s.encode())
print(conn.recv())