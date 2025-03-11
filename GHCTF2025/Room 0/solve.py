def KSA(key):
    """ Key-Scheduling Algorithm (KSA) 密钥调度算法"""
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S, key):
    """ Pseudo-Random Generation Algorithm (PRGA) 伪随机数生成算法"""
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256] ^ key[i&7]
        yield K


def RC4(key, text):
    """ RC4 encryption/decryption """
    S = KSA(key)
    keystream = PRGA(S, key)
    res = []
    for char in text:
        res.append(char ^ next(keystream))
    return bytes(res)

# xor=[0x75,0x5f,0xf0,0xd3]
# addr=0x401000
# for i in range(0x600):
#     idc.patch_byte(addr+i, ord(idc.get_bytes(addr+i, 1))^xor[i%4])


key = [0xD4, 0x35, 0x6D, 0xF8, 0xF8, 0x6D, 0x35, 0xD4]
text = [0x22, 0xC4, 0xA0, 0x5A, 0xDE, 0xED, 0x62, 0x5E, 0x25, 0xE2, 0x6D, 0xA6, 0x05, 0xA7, 0x20, 0x8D, 0x7D, 0x99, 0x52, 0x3E, 0x8C, 0xA7, 0x7F, 0xFA, 0x09, 0xD8, 0x62, 0xDB, 0x00, 0x80, 0xC2, 0xA9]
print(RC4(key, text))

# def check_key(key):
#     v2 = key
#     v6 = 0
#     v9 = v2
#     v8 = v2>>24
#     v5 = (v2>>16)&0xff
#     v4 = (v2>>8)&0xff
#     for i in range(32):
#         v7 = v6 * ((v8 + 1415881080)&0xffffffff) * ((v9 - 1467486175)&0xffffffff) * (((v8 - v9)&0xffffffff) ^ (v8 >> 4))
#         v7 &= 0xffffffff
#         v5 = ((v9 + v5)&0xffffffff) ^ ((8 * v4)&0xffffffff)
#         v4 = ((v9 + v8)&0xffffffff) ^ ((8 * v5)&0xffffffff)
#         v8 = ((v9 + v4)&0xffffffff) ^ ((8 * v5)&0xffffffff)
#         v9 -= ((v4 + v5 + v8)&0xffffffff)
#         v9 &= 0xffffffff
#         v6 = v7 + ((v8 + 1467486175)&0xffffffff) * ((((v8 - v9)&0xffffffff) ^ (v8 >> 4)) // ((v9 - 1415881080)&0xffffffff))
#         return v9 ^ v6
#
# for i in range(0xffffffff):
#     if check_key(i) == 289739801:
#         print(hex(i))
from z3 import *
s = Solver()
v9 = BitVec('v9', 32)
v8 = (v9 >> 24) & 0xff
v5 = (v9 >> 16) & 0xff
v4 = (v9 >> 8) & 0xff
v5 = (v9 + v5) ^ (8 * v4)
v4 = (v9 + v8) ^ (8 * v5)
v8 = (v9 + v4) ^ (8 * v5)
v9 -= v4 + v5 + v8
s.add(v9==0x5464A178)
if s.check() == sat:
    m = s.model()
    print(hex(m[m[0]].as_long()))