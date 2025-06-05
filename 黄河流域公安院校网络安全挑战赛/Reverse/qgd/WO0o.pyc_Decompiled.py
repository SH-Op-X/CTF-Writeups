# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: WO0o.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from secret import decrypt
key = bytes.fromhex('EC3700DFCD4F364EC54B19C5E7E26DEF6A25087C4FCDF4F8507A40A9019E3B48BD70129D0141A5B8F089F280F4BE6CCD')
ciphertext = b'\xd4z\'0L\x10\xca\x0b\x0b\xaa\x15\xbeK0"\xbf\xb2\xc6\x05'
cipher = decrypt(ciphertext, key)
a = bytes(input('flag呢'), encoding='utf-8')
if a == cipher:
    print('没错没错')
else:
    print('不对不对')