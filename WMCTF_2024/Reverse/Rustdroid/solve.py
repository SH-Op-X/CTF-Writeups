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


def move(x, bit, xor):
    x ^= xor
    return ((x >> (8 - bit)) | (x << bit)) & 0xff

def RC4(key, text):
    """ RC4 encryption/decryption """
    S = KSA(key)
    keystream = PRGA(S)
    res = []
    b = [0x77, 0x88, 0x99, 0x66]
    for i in range(len(text)):
        char = text[i]
        char = char ^ next(keystream)
        char = move(char, 5, b[i&3])
        char = move(char, 4, 0xde)
        char = move(char, 3, 0xad)
        char = move(char, 2, 0xbe)
        char = move(char, 1, 0xef)
        res.append(char)
    return bytes(res), len(res)


if __name__ == "__main__":
    key = b"fun@eZ"
    v = [0x4E4FCE594215BA1F, 0x0C745BAE69BFD994, 0x87081E9C7F8AFCC0, 0x2BB08F87F5646BF5, 0x29FF53E2]
    text = []
    for i in v:
        while i:
            text.append(i&0xff)
            i >>= 8
    print(text, len(text))
    print(RC4(key, text))
