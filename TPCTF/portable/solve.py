s = [0x34, 0x2A, 0x42, 0x0E, 0x00, 0x1D, 0x5C, 0x33, 0x5E, 0x44, 0x3E, 0x1A, 0x0B, 0x5C, 0x2C, 0x3A, 0x5F, 0x22, 0x03, 0x28, 0x36, 0x1B, 0x07, 0x31, 0x8D, 0xDE, 0x10, 0xA2, 0xEB, 0xB2, 0xDA, 0xA2, 0xD8, 0x18, 0x0D, 0x17, 0x1C, 0x1F, 0xBD, 0xD9, 0x1D, 0xBF, 0xEB, 0xA2, 0xD8, 0x16, 0x0D, 0xA0, 0xF6, 0x30, 0xBD, 0xD8, 0x17, 0xBE, 0xDA, 0x0F, 0xAB, 0xC1, 0xAE, 0xEA, 0x8D, 0xDE, 0x11, 0x01, 0xA1, 0xC5]
xor = b"Cosmopolitan"
flag = []
for i in range(len(s)):
    flag.append((xor[i%len(xor)]^s[i]))
print(f"TPCTF{{{bytes(flag).decode("utf-8")}}}")