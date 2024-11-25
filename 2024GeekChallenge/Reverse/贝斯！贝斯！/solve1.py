import base64

from Crypto.Util.number import bytes_to_long

correct_table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'
table = 'eM+wr=x8aYZ/[zU$yRB&kbO;%p0P5f*7d(n]1Eug4ojc62AC,v39!h-^qQ.G?s)i:DFlS<>#@HINJTmtKLVWX'
c = 'RjB6Myu#,>Bgoq&u.H(nBgdIaOKJbgEYj1GR4S.w'
new_c = []
for i in range(len(c)):
    new_c.append(correct_table[table.index(c[i])])
base85_c = base64.b85decode(''.join(new_c))
print(base85_c) # 6pmB34FC9sbYxcKP9rjGGiyRsx1s6c72

# base64 s x
# Base58 字符集
BASE58_ALPHABET = "gJHTDQsbpyAr14u9zoiX3YvtxdhBk6KRZNjV82WSeLfPUnCaMFwEqGc75m"


def custom_base58_encode(input_string):
    # 初始化字符表
    base58_alphabet = "gJHTDQsbpyAr14u9zoiX3YvtxdhBk6KRZNjV82WSeLfPUnCaMFwEqGc75m"

    # 计算输出缓冲区大小 `v7`
    v7 = 138 * len(input_string) // 100 + 1

    # 初始化 Block 和 v5，模拟 C 代码中的 malloc
    block = [0] * v7
    encoded_result = [""] * v7

    # `v10` 用于遍历 input_string，`v8` 为 encoded_result 的索引
    v10 = 0

    while v10 < len(input_string):
        v9 = ord(input_string[v10])  # 当前字符的 ASCII 值
        # 类似于进制转换，将每个字符映射到 Base58 字符集中
        for i in range(v7 - 1, -1, -1):
            v9 += block[i] << 8  # 左移以累加 ASCII 值
            block[i] = v9 % 58  # 取余以限制在 Base58 范围内
            v9 //= 58  # 整除以进行进位
            if v9 == 0:
                break
        v10 += 1
    # print(block)
    # 处理前导零
    i = 0
    while i < v7 and block[i] == 0:
        i += 1

    # 将编码结果填充到 encoded_result 中
    v8 = 0
    while i < v7:
        encoded_result[v8] = base58_alphabet[block[i]]
        v8 += 1
        i += 1

    # 组合成最终字符串，模拟 C 中的 null-terminated 字符串
    return ''.join(encoded_result[:v8])


def custom_base58_decode(encoded_string):
    # 初始化 Base58 字符表和字符映射
    base58_alphabet = "gJHTDQsbpyAr14u9zoiX3YvtxdhBk6KRZNjV82WSeLfPUnCaMFwEqGc75m"
    base58_index = {char: index for index, char in enumerate(base58_alphabet)}

    # 计算 Block 缓冲区大小 `v7`
    v7 = 138 * len(encoded_string) // 100 + 1
    # print(v7)
    v7 = 39
    # 初始化 Block
    block = [0] * v7

    for i in range(len(encoded_string)):
        block[i] = base58_index[encoded_string[i]]

    # 遍历编码字符串
    for char in encoded_string:
        # 获取字符在 Base58 中的数值
        v9 = base58_index[char]
        # 反向进行进制转换
        for i in range(v7 - 1, -1, -1):
            v9 += block[i] * 58
            block[i] = v9 & 0xFF  # 取低8位
            v9 >>= 8  # 右移8位以进行进位
        # 确保每个字符被完全转换

    # 去除前导零字节，转换为字节数组
    leading_zeros = 0
    while leading_zeros < v7 and block[leading_zeros] == 0:
        leading_zeros += 1

    # 提取有效字节并转换为字节数组
    decoded_bytes = bytes(block[leading_zeros:])
    return decoded_bytes.decode('utf-8', errors='ignore')


print(custom_base58_encode("aaaaaaaaaaaaaaaaaaaa\n"))
print(custom_base58_encode("SYC{baaaaaaaaaaaaaaaaaa}"))
print(custom_base58_encode("SYC{baaadaaaaaaaaaaaaaa}"))
print(custom_base58_encode("SYC{baaabbaaaaaaaaaaaaa}"))
print(custom_base58_encode("SYC{baaaabbaaaaaaddaaad}"))

# from itertools import product
# from string import ascii_letters, digits
#
# char_list = ascii_letters + digits
# for i in product(char_list, repeat=4):
#     if "6pmB34FC9s" == custom_base58_encode("SYC{"+"".join(i)+"a"*16)[:10]:
#         print("".join(i))
# print(custom_base58_decode("6pmB34FC9sbYxcKP9rjGGiyRsx1s6c72"))
# print(custom_base58_decode("J3SFQX76Y7UUBYdrGtnMq75p3H2g"))

