import struct
from ctypes import c_uint32


def tea_decrypt(r, v, key, delta):
    v0, v1 = c_uint32(v[0]), c_uint32(v[1])
    total = c_uint32(delta * r + 0xC6EF3720)
    for i in range(r):
        total.value -= delta
        v0.value += ((v1.value << 4) + key[0]) ^ (v1.value + total.value) ^ ((v1.value >> 5) + key[1])
        v1.value += ((v0.value << 4) + key[2]) ^ (v0.value + total.value) ^ ((v0.value >> 5) + key[3])
    return v0.value, v1.value


def KSA(key):
    """ Key-Scheduling Algorithm (KSA) 密钥调度算法"""
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S):
    """ Pseudo-Random Generation Algorithm (PRGA) 伪随机数生成算法"""
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key, text):
    """ RC4 encryption/decryption """
    S = KSA(key)
    keystream = PRGA(S)
    res = []
    for char in text:
        res.append(char ^ next(keystream))
    return bytes(res)


if __name__ == '__main__':
    v = [0x11223344, 0x55667788]
    k = [0x123, 0x4567, 0x89ab, 0xcdef]
    for i in range(0, len(v), 2):
        v[i:i + 2] = tea_decrypt(32, v[i:i + 2], k, 0x61C88647)
    print(list(map(hex, v)))
    key = struct.pack(">I", v[0])+struct.pack(">I", v[1])
    print(list(key))
    text = [0x14, 0xA6, 0x91, 0xFE, 0xB9, 0xD7, 0x41, 0xAF, 0x82, 0xCC, 0x4E, 0xE9, 0x47, 0x47, 0x28, 0x4F, 0xD1]
    print(RC4(key, text))
    print(RC4(key, text).decode())
