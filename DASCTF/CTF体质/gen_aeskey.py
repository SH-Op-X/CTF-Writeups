s = [0x0B, 0xCF, 0x79, 0x7E, 0xC7, 0xEA, 0x5F, 0x31, 0xBC, 0xEE, 0xE7, 0x0B, 0x1E, 0x91, 0xAA, 0xDD, 0x6F, 0x07, 0xC1, 0x10, 0x36, 0x75, 0x20, 0x06, 0x32, 0xE3, 0xD0, 0x66, 0xB8, 0x7D, 0xFC, 0x90]
import struct


def byte_to_int_arr(byte_data):
    """将byte数组（大端序）转换为int数组"""
    # 每个int是4个字节，所以长度是 byte_data_len / 4
    num_ints = len(byte_data) // 4
    # '>{}I'.format(num_ints) 表示以大端序解码 num_ints 个无符号整数
    return list(struct.unpack('>' + 'I' * num_ints, byte_data))


def int_arr_to_byte(int_data):
    """将int数组转换为byte数组（大端序）"""
    byte_result = b''
    for i in int_data:
        # '>I' 表示以大端序打包一个无符号整数
        # [0xFFFFFFFF]是为了处理python中整数的溢出，确保是32位无符号数
        byte_result += struct.pack('>I', i & 0xFFFFFFFF)
    return byte_result


def decrypt(ciphertext_bytes, key, times):
    """
    解密函数
    :param ciphertext_bytes: 密文字节数组
    :param key: 包含4个整数的密钥列表
    :param times: 迭代次数
    :return: 明文字节数组
    """
    # 将密文从 bytes 转换为 int 列表
    # 24字节的密文会变成6个整数
    temp_int = byte_to_int_arr(ciphertext_bytes)
    decrypted_int = []

    # 按8字节（2个int）为一块进行处理
    for h in range(0, len(temp_int), 2):
        y, z = temp_int[h], temp_int[h + 1]

        # 获取密钥
        a, b, c, d = key[0], key[1], key[2], key[3]

        # 定义delta
        delta = 305419896
        # sum的初始值是加密结束时的值
        s = (delta * times) & 0xFFFFFFFF

        # 执行解密循环
        for i in range(times):
            # 先解密 z
            z = (z - (((((y << 2) & 0xFFFFFFFF) + c) ^ (y + s) & 0xFFFFFFFF) ^ (((y >> 7) & 0xFFFFFFFF) + d)) ^ (
                        39 - b)) & 0xFFFFFFFF
            # 更新 sum
            s = (s - delta) & 0xFFFFFFFF
            # 再解密 y
            y = (y - (((((z << 3) & 0xFFFFFFFF) + a) ^ (z + s) & 0xFFFFFFFF) ^ (((z >> 6) & 0xFFFFFFFF) + b)) ^ (
                        54 - a)) & 0xFFFFFFFF

        decrypted_int.extend([y, z])

    # 将解密后的 int 列表转换回 bytes
    return int_arr_to_byte(decrypted_int)

# 1. 准备密文
# Java的byte是-128到127，Python需要转换
signed_bytes = [34, 111, 123, -86, -94, -83, 54, 49, 25, 12, -118, 21, 65, -26, 25, -94, 101, 96, -24, 101, -58,
                113, 13, -12]
# 将有符号byte转为无符号byte (0-255)
ciphertext = bytes([b & 0xff for b in signed_bytes])

# 2. 准备密钥
# "flag" -> 0x666c6167
key = [0x66, 0x6c, 0x61, 0x67][::-1]

# 3. 设定迭代次数
times = 32

# 4. 执行解密
plaintext_bytes = decrypt(ciphertext, key, times)

# 5. 输出结果
print("解密后的字节流:", plaintext_bytes)
try:
    # 尝试用UTF-8解码，flag通常是可见字符
    print("解密后的字符串:", plaintext_bytes.decode('utf-8'))
except UnicodeDecodeError:
    print("解密结果无法用UTF-8解码。")

dword = []
for i in range(256):
    v1 = i
    for j in range(8):
        if (v1 & 1) != 0:
            v1 = (v1 >> 1) ^ 0xEDB88320
        else:
            v1 >>= 1
    dword.append(v1)
print(dword)