s = [0x23, 0x29, 0x1E, 0x24, 0x38, 0x0E, 0x15, 0x20, 0x37, 0x0E, 0x05, 0x20, 0x00, 0x0E, 0x37, 0x12, 0x1D, 0x0F, 0x24, 0x01, 0x01, 0x39]
print(len(s))
xor = [69, 69, 127, 67, 67, 68]
for i in range(len(s)):
    if s[i] == 1:
        s[i] = ord("=")
        continue
    if s[i] == 0x38:
        s[i] = ord("{")
        continue
    if s[i] == 0x39:
        s[i] = ord("}")
        continue
    if s[i] == 0x1c:
        s[i] = ord("1")
        continue
    if s[i] == 0x1d:
        s[i] = ord("2")
        continue
    if s[i] + 67 in list(range(97, 123)):
        s[i] += 67
    elif s[i] + 63 in list(range(65, 91)):
        s[i] += 63
from base64 import b64decode
for i in ["0", "3", "4", "5", "6", "7", "8", "9"]:
    s[12] = ord(i)
    print("".join(map(chr, s)))
    print(b64decode("".join(map(chr, s[5:-1])).encode()))