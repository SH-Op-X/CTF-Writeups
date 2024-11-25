from pwn import *

r = remote('nc1.ctfplus.cn', 42948)
def bruteforce():
    flag = ''
    total = 32 - 1
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}-~!?#%&@abcdefghijklmnopqrstuvwxyz'

    r.recvuntil(b'[-] ')
    while True:
        payload = '1' * (total - len(flag))
        r.sendline(b"yes")
        r.recvuntil(b'[-] ')
        r.sendline(payload.encode())
        ciphertext_1 = r.recvuntil(b'[-] ').split(b":")[-1].split(b"\n")[0]
        # print(ciphertext_1)
        for c in chars:
            r.sendline(b"yes")
            r.recvuntil(b'[-] ')
            # print(payload + flag + c)
            r.sendline((payload + flag + c).encode())
            ciphertext_2 = r.recvuntil(b'[-] ').split(b":")[-1].split(b"\n")[0]
            # Comapare the middle blocks ([32:64]) of each encrypted text
            if ciphertext_2[32:64] == ciphertext_1[32:64]:
                flag += c
                print(flag)
                break

bruteforce()
