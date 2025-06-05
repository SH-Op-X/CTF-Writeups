from Crypto.Util.number import bytes_to_long

def transpose_bytes8x8(block):
    # 先把 block 解开成 8×8 位矩阵 bits[row][col]
    bits = [[(block[row] >> (7 - col)) & 1 for col in range(8)]
            for row in range(8)]

    # 转置后按行重组，每行 8 个 bit 合成一个字节
    transposed = []
    for new_row in range(8):
        byte = 0
        for new_col in range(8):
            byte = (byte << 1) | bits[new_col][new_row]
        transposed.append(byte)

    return bytes(transposed)


s = ["08ADD5C04E5934C8", "199AC0E6DA4C2BC9", "FF83F5E87D5510B5", "58447D6AD4E38B74"]
for i in range(len(s)):
    s[i] = transpose_bytes8x8(bytes.fromhex(s[i])[::-1])
ss = []
for i in s:
    ss += list(i)
for i in range(len(ss)):
    ss[i] = (ss[i] << 3) | (ss[i] >> 5)
    ss[i] &= 0xff
s = [bytes_to_long(bytes(ss[i:i+8][::-1])) for i in range(0, len(ss), 8)]
new_s = []
for v in s:
    for i in range(64):
        bit = v & 1
        if bit:
            v ^= 0x2EF20D07161E85F7
        v >>= 1
        if bit:
            v |= 0x8000000000000000
    new_s.append(v)
s = []
for i in new_s:
    tmp = list(i.to_bytes(8, byteorder='big'))
    flag = [0] * 8
    for i in range(0, 6, 3):
        flag[i+2] = tmp[i+2] ^ tmp[i+1]
        flag[i] = tmp[i] ^ flag[i+2]
        flag[i+1] = tmp[i+1] ^ flag[i]
    flag[6] = tmp[6]
    flag[7] = tmp[7]
    print("".join(map(chr, flag)), end="")
print()