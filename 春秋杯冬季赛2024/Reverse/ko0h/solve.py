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
        res.append((char + next(keystream))&0xff)
    return bytes(res)


key = b"DDDDAAAASSSS"
text = [24, -100, 71, 61, 59, -31, 41, 39, -97, 52, -125, -43, -19, -75, ord("n"), ord("Y"), 127, -34, 71, -41, 101, 63, 122, 51, 91, 100, -74, -6, -108, 85, -121, 66, 32, 6, 12, 105, -2, 114, -87, -28, -47, 124]
print(RC4(key, text).decode())
