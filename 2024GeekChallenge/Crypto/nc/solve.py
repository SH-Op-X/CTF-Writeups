from pwn import *
import re
import string
import itertools
from hashlib import sha256

r = remote("nc1.ctfplus.cn", port=15302)
content = r.recvuntil(b": ").decode()
print(content)
proof = re.findall(r'X\+(.*?)\)', content)[0]
sha256_value = re.findall(r'== (.*?)\n', content)[0]
choices = string.ascii_letters+string.digits
flag = []
for c in itertools.product(choices, repeat=4):
    if sha256(("".join(c)+proof).encode()).hexdigest() == sha256_value:
        print("".join(c))
        r.sendline("".join(c).encode())
        r.recvuntil(b"[-] ")
        for i in range(1, 33):
            r.sendline(str(i).encode())
            content = r.recvuntil(b"[-] ")
            flag.append(content)
        break
flag = "".join(chr(i[4]) for i in flag)
print(flag)
