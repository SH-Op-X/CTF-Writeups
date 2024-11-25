import math

from Crypto.Util.number import long_to_bytes
import gmpy2
from gmpy2 import gcd

key = b"IKnowYouLikeCrypto"
for i in range(4):
    with open(f"output/cmp{i}.enc", "r") as f:
        enc_data = f.read()
    enc_data = list(eval(enc_data))
    for j in range(len(enc_data)):
        enc_data[j] ^= key[j%len(key)]
    data = bytes(enc_data).decode().split()
    p = int(data[0][2:], 16)
    q = int(data[1][2:], 16)
    e = int(data[2][2:], 16)
    # e = (e >> 8) | (e << 8 & 0xffff)
    c = int(data[3][2:], 16)
    # print(p, q, e, c)
    n = p * q
    phi = (p - 1) * (q - 1)
    gongyue = gcd(phi, e)
    d = gmpy2.invert(e // gongyue, phi)
    m = pow(c, d, n)
    m = gmpy2.iroot(m, gongyue)[0]
    #     if (p-1) % 3 == 0:
    #         d = gmpy2.invert(e, q-1)
    #     else:
    #         d = gmpy2.invert(e, p-1)
    # if gcd(p-1, e) > 1:
    #     d = gmpy2.invert(e, q-1)
    # else:
    #     d = gmpy2.invert(e, p-1)
    # m = pow(c, d, n)
    # if i == 2:
    #     m = math.pow(m, 1/3)
    print(hex(m))
