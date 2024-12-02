text = [57,
		244,
		117,
		200,
		213,
		87,
		194,
		195,
		164,
		100,
		103,
		63,
		19,
		79,
		137,
		70,
		201,
		24,
		163,
		129,
		237,
		210,
		5,
		19,
		35,
		21]
key = b"LZSDS"

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
        K = (S[i] + S[j]) % 256
        yield K


def RC4(key, text):
    """ RC4 encryption/decryption """
    S = KSA(key)
    keystream = PRGA(S)
    res = []
    for char in text:
        res.append(char ^ next(keystream))
    return bytes(res)


out = RC4(key, text).decode()
flag = ""
for i in range(0, len(out), 2):
	flag += out[i]
from base64 import b64encode
print("LZSDS{"+b64encode(flag.encode()).decode()+"}")