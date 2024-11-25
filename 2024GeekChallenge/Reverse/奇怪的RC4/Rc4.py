def KSA(key):
    j = 0
    S = list(range(256))
    key_length = len(key)
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = (S[i] + S[j]) % 256
        yield k


def rc4(plaintext, key):
    key = [ord(i) for i in key]
    # plaintext = [ord(i) for i in plaintext]
    S = KSA(key)
    xor_value = PRGA(S)
    for i in range(len(plaintext)):
        plaintext[i] ^= int(next(xor_value)) + 6
    for i in range(len(plaintext)):
        plaintext[i] -= i
    return plaintext
