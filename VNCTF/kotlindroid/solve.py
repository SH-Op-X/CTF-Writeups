s = [0x76, 99, 101, 0x7E, 0x7C, 0x72, 110, 100]
for i in s:
    print(chr(i^23), end="")
print(s)

s = [0x7B, 0x71, 109, 99, 97, 0x7A, 0x7C, 105]
for i in s:
    print(chr(i^8), end="")
print(s)
print(bytes(s).hex())
print(bytes([49, 49, 52, 53, 49, 52]))