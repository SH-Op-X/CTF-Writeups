plain = "When I coming to SCU, I feel so cool! XOR is amazing, isn\'t it?"
# plain = "abc"
ori_cipher = ''
for i in range(len(plain)):
    ori_cipher += bin(ord(plain[i]))[2:].zfill(8)
# for i in range(len(ori_cipher)):
#     tmp = int(ori_cipher[i])
#     for j in range(i, len(ori_cipher)):
#         tmp ^= int(ori_cipher[j])
#     ori_cipher = ori_cipher[:i] + str(tmp) + ori_cipher[i+1:]
# print(ori_cipher)

# cipher = ori_cipher
cipher = "1001101001001111101110001011010000111111100011100011111110111101101101011011011001001110010011111011101000110111101001111011010111100000011000100111110110011001110110000111111110001110001111111011101110111001101110011011011111000000010111011011010111000000010000100100101001001000011010000011111000111111100100000111010110011100001111111011000110000010001111111011111001001001101111100101001110110001101101000100010111001000001111111011000010100010010010111100010110100111110000000100111001011000001010100110001001111101100110011000001001100111100001000101001001011001101111011010011001101010010011100010001001101010010111011101111110010101101101011101111110110101101101111100000110101111110111111010001110010101110111100101110110010101110100000100100111011000010100111101111001001011101110100111111001110110"
cipher = list(cipher)  # 将字符串转为可变列表
for i in range(len(cipher)-1, -1, -1):  # 从末尾向前遍历
    tmp = int(cipher[i])
    for j in range(i + 1, len(cipher)):  # XOR 从 i+1 到结尾的位
        tmp ^= int(cipher[j])
    cipher[i] = str(tmp)
# 转换为原始二进制序列
binary_plain = "0"+"".join(cipher)[:-1]
print(binary_plain)
print(binary_plain[:504])
diff = 0
for i in range(503):
    if binary_plain[i] != ori_cipher[i] and binary_plain[i+1] != ori_cipher[i+1]:
        diff += 1
print(diff)
# 每 8 位恢复一个字符
plain = "".join([chr(int(binary_plain[i:i+8], 2)) for i in range(0, len(binary_plain), 8)])
print(plain)
# Whdî I comihg,toSCU4@I feel so col\! XOR iC amazing, hón't it?SCUCTF{ucu_i3_s0_o0ol!x0r_1s_8m4z1ngAM

for i in range(1, 6):
    s = list(bin(ord("u")))
    s[i] = "1" if s[i] == "0" else "0"
    s[i+1] = "1" if s[i+1] == "0" else "0"
    print(chr(int("".join(s), 2)), end=", ")
print()
for i in range(1, 6):
    s = list(bin(ord("o")))
    s[i] = "1" if s[i] == "0" else "0"
    s[i+1] = "1" if s[i+1] == "0" else "0"
    print(chr(int("".join(s), 2)), end=", ")
print()
for i in range(1, 6):
    s = list(bin(ord("8")))
    s[i] = "1" if s[i] == "0" else "0"
    s[i+1] = "1" if s[i+1] == "0" else "0"
    print(chr(int("".join(s), 2)), end=", ")
print()
for i in range(1, 6):
    s = list(bin(ord("A")))
    s[i] = "1" if s[i] == "0" else "0"
    s[i+1] = "1" if s[i+1] == "0" else "0"
    print(chr(int("".join(s), 2)), end=", ")