# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: secret.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

def key_schedule(key: bytes) -> list:
    S = list(range(128))
    v6 = 0
    for j in range(128):
        v6 = (S[j] + key[j % len(key)] + v6) % 128
        v6 = (v6 ^ 55) % 128
        S[j], S[v6] = (S[v6], S[j])
    return S

def next_byte(state: dict) -> int:
    S = state['S']
    state['i'] = (state['i'] + 1) % 128
    state['j'] = (state['j'] + S[state['i']]) % 128
    S[state['i']], S[state['j']] = (S[state['j']], S[state['i']])
    v2 = S[(S[state['i']] + S[state['j']]) % 128]
    return (16 * v2 | v2 >> 4) & 255

def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    state = {'S': key_schedule(key), 'i': 0, 'j': 0}
    plaintext = bytearray()
    for byte in ciphertext:
        plaintext.append(byte ^ next_byte(state))
    return bytes(plaintext)

key = bytes.fromhex('EC3700DFCD4F364EC54B19C5E7E26DEF6A25087C4FCDF4F8507A40A9019E3B48BD70129D0141A5B8F089F280F4BE6CCD')
ciphertext = b'\xd4z\'0L\x10\xca\x0b\x0b\xaa\x15\xbeK0"\xbf\xb2\xc6\x05'
flag2 = decrypt(ciphertext, key).decode()

b = bytes.fromhex("48 89 4C 24 08 55 57 48 81 EC 28 01 00 00 48 8D 6C 24 20 48 8D 0D 34 08 01 00 E8 96 FB FF FF 48 83 BD 20 01 00 00 00 75 05 E9 BF 00 00 00 48 8B 8D 20 01 00 00 E8 7D F9 FF FF 48 89 45 08 48 C7 45 28 00 00 00 00 EB 0B 48 8B 45 28 48 FF C0 48 89 45 28 48 8B 45 08 48 39 45 28 0F 83 8C 00 00 00 48 8B 45 28 48 FF C0 33 D2 B9 02 00 00 00 48 F7 F1 48 8B C2 48 83 F8 01 75 2A 48 8B 45 28 48 8B 8D 20 01 00 00 48 03 C8 48 8B C1 0F BE 00 83 F0 31 48 8B 4D 28 48 8B 95 20 01 00 00 48 03 D1 48 8B CA 88 01 48 8B 45 28 48 FF C0 33 D2 B9 02 00 00 00 48 F7 F1 48 8B C2 48 85 C0 75 2A 48 8B 45 28 48 8B 8D 20 01 00 00 48 03 C8 48 8B C1 0F BE 00 83 F0 58 48 8B 4D 28 48 8B 95 20 01 00 00 48 03 D1 48 8B CA 88 01".replace(" ", ""))
with open("out", "wb") as f:
    f.write(b)

flag1 = ""
encrypted = [88,47,80,54,95,57,90,54,94,47]
for i in range(len(encrypted)):
    if i%2:
        flag1 += chr(encrypted[i]^0x58)
    else:
        flag1 += chr(encrypted[i]^0x31)
print(f"flag{{{flag1+flag2}}}")
