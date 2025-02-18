s = [101, 74, 76, 49, 101, 76, 117, 87, 55, 69, 118, 68, 118, 69, 55, 67, 61, 83, 62, 111, 81, 77, 115, 101, 53, 73, 83, 66, 68, 114, 109, 108, 75, 66, 97, 117, 93, 127, 115, 124, 109, 82, 93, 115]
print(len(s))
for i in range(len(s)):
    s[i] = (s[i]^7)-1
print(bytes(s))
from base64 import b64decode
text = b64decode(bytes(s))



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


def RC4(key, text, i):
    """ RC4 encryption/decryption """
    S = KSA(key)
    keystream = PRGA(S)
    res = []
    for char in text:
        res.append(char ^ next(keystream) ^ i)
    return bytes(res)



key = b"Take_it_easy"
text = RC4(key, text, 40)
for i in range(len(text)):
    print(chr(text[i]-3), end="")