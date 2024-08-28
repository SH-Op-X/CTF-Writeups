s = "Xsl3BDxP"
flag = []
for i in range(len(s)):
    tmp = ord(s[i])^0x33
    if i % 3 == 2:
        flag.append(tmp+37)
    elif i % 3 == 1:
        flag.append(tmp-16)
    else:
        flag.append(tmp^0x5a)
flag.append(ord("-"))
s = "mzXaPLzR"
for i in range(len(s)):
    if ord(s[i]) < 65 + 26:
        if ord(s[i])-65+48<65:
            flag.append(ord(s[i])-65+48+26)
        else:
            flag.append(ord(s[i])-65+48)
    else:
        if ord(s[i])-97+92<97:
            flag.append(ord(s[i])-97+92+26)
        else:
            flag.append(ord(s[i])-97+92)
print(flag)
content = bytes(flag) + b'\n'
print(content, len(content))

from pwn import *

conn = remote("challs.tfcctf.com", 32303)
# conn.recvuntil(b"Please enter your license key to use this program!\n")
conn.sendline(content)
print(conn.recv())