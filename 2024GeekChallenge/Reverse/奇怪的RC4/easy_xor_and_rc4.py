# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.19 | packaged by conda-forge | (default, Mar 20 2024, 12:38:07) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: easy_xor_and_rc4.py
from Rc4 import *

def xor1(plaintext, xor_list):
    try:
        xor_list = [ord(i) for i in xor_list]
    except:
        pass
    else:
        try:
            plaintext = [ord(i) for i in plaintext]
        except:
            pass
        else:
            for i in range(len(plaintext)):
                plaintext[i] ^= xor_list[i]
            else:
                return plaintext


def xor2(plaintext):
    try:
        plaintext = [ord(i) for i in plaintext]
    except:
        pass
    else:
        for i in range(len(plaintext) - 1):
            plaintext[i + 1] = plaintext[i] ^ plaintext[i + 1]
        else:
            return plaintext


def enc(plaintext, key, xor_list):
    plaintext = rc4(plaintext, key)
    plaintext = xor1(plaintext, xor_list)
    plaintext = xor2(plaintext)
    return plaintext


plaintext = input("please give your input:")
key = "SYCFOREVER"
xor_list = list(range(len(plaintext)))
cipher = [158, 31, 205, 434, 354, 15, 383, 298, 304, 351, 465, 312, 261, 442, 
 397, 474, 310, 397, 31, 21, 78, 67, 47, 133, 168, 48, 153, 99, 103, 
 204, 137, 29, 22, 13, 228, 3, 136, 141, 248, 124, 26, 26, 65, 200, 
 7]
plaintext = enc(plaintext, key, xor_list)
for i in range(len(cipher)):
    if cipher[i] != plaintext[i]:
        print("Wrong")
        exit(1)
else:
    print("You know the flag!!")

# okay decompiling .\easy_xor_and_rc4.pyc
