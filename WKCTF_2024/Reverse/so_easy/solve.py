s = [0x540A95F0C1BA81AE, 0xF8844E52E24A0314, 0x09FD988F98143EC9, 0x3FC00F01B405AD5E]
new_s = []
for v10 in s:
    for i in range(255):
        bit = v10 & 1
        if bit:
            v10 ^= 0x71234EA7D92996F5
        v10 >>= 1
        if bit:
            v10 |= 0x8000000000000000
    new_s.append(v10)
print("".join([bytes.fromhex(hex(i)[2:]).decode()[::-1] for i in new_s]))