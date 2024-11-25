from Rc4 import *


def xor1(plaintext, xor_list):
    # xor_list = [ord(i) for i in xor_list]
    # plaintext = [ord(i) for i in plaintext]
    for i in range(len(plaintext)):
        plaintext[i] ^= xor_list[i]
    return plaintext


def xor2(plaintext):
    # plaintext = [ord(i) for i in plaintext]
    for i in range(len(plaintext) - 1, 0, -1):
        plaintext[i] = plaintext[i] ^ plaintext[i-1]
    return plaintext


def enc(plaintext, key, xor_list):
    plaintext = xor2(plaintext)
    plaintext = xor1(plaintext, xor_list)
    plaintext = rc4(plaintext, key)
    return plaintext


key = "SYCFOREVER"
cipher = [158, 31, 205, 434, 354, 15, 383, 298, 304, 351, 465, 312, 261, 442, 397, 474, 310, 397, 31, 21, 78, 67, 47, 133, 168, 48, 153, 99, 103, 204, 137, 29, 22, 13, 228, 3, 136, 141, 248, 124, 26, 26, 65, 200, 7]
xor_list = list(range(len(cipher)))
plaintext = enc(cipher, key, xor_list)
print("".join(map(chr, cipher)))
