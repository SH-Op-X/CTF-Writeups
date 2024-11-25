import struct


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


if __name__ == "__main__":
    key = b"syclover"
    text = [0xA67A02C9047D5B94, 0x7EF9680DBC980739, 0x7104F81698BFBD08, 0x61DB8498B686155F]
    text = b"".join([struct.pack("<Q", text[i]) for i in range(len(text))])
    print(len(text))
    text = RC4(key, text)
    flag = ""
    for i in range(len(text)):
        flag += chr(text[i]^0x14)
    print(flag)
