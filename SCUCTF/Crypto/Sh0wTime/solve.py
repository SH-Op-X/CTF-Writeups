from pwn import *
from datetime import datetime
from ecdsa.ecdsa import Public_key, Private_key, Signature, generator_192
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
import json

g = generator_192
n = g.order()

io = remote('223.129.86.2', 33886)
io.recvuntil(b"Enter your option: ")
def send_payload(time):
    while True:
        now = datetime.now()
        if now.strftime("%S") == time:
            io.sendline(b"sign_time")
            return json.loads(io.recvline().decode().replace("\n", "").replace("'", "\""))
        sleep(1)

def sha1(data):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data)
    return sha1_hash.digest()

# Send first payload, time we want is 02
signature_1 = send_payload("01")
print(signature_1)
msg_1 = bytes_to_long(sha1(signature_1['time'].encode()))

temp = Signature(int(signature_1['r'], 16), int(signature_1['s'], 16))
r = int(signature_1['r'], 16)
s = int(signature_1['s'], 16)
# There are two possible public keys from the signature observed
public_key_1, public_key_2 = temp.recover_public_keys(msg_1, g)
print(public_key_1, public_key_2)

inv = inverse(r, n)
secret = ((s * 100 - msg_1) * inv) % n
print(secret)
io.recvuntil(b'Enter your option: ')
io.sendline(b'I kown the secret')
print(io.recv())
io.sendline(hex(secret).encode())
print(io.recv())
