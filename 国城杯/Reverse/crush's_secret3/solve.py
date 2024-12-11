import struct
from ctypes import c_uint32
"""
参数描述:
  DELTA: 神秘常数δ，它来源于黄金比率，以保证每一轮加密都不相同。但δ的精确值似乎并不重要，这里 TEA 把它定义为 δ=「(√5 - 1)231」
      v: 需要加解密的数据，格式为32位的无符号整数组成的数组
      n: n表示需要加密的32位无符号整数的个数（例：n为1时，只有v数组中的第一个元素被加密了），n不能大于v的长度
      k: 密钥，格式为4个32位无符号整数组成的数组，即密钥长度为128位
"""

def xxtea_encrypt(n, v, key):
    # 全部转为c_unit32格式
    v = [c_uint32(i) for i in v]
    r = 6 + 52 // n
    v1 = v[n-1].value
    delta = 0x9e3779b9
    total = c_uint32(0)
    for i in range(r):
        total.value += delta
        e = (total.value >> 2) & 3
        for j in range(n-1):
            v0 = v[j+1].value
            v[j].value += ((((v1 >> 5) ^ (v0 << 2)) + ((v0 >> 3) ^ (v1 << 4))) ^ ((total.value ^ v0) + (key[(j & 3) ^ e] ^ v1)))
            v1 = v[j].value
        v0 = v[0].value
        v[n-1].value += ((((v1 >> 5) ^ (v0 << 2)) + ((v0 >> 3) ^ (v1 << 4))) ^ ((total.value ^ v0) + (key[((n-1) & 3) ^ e] ^ v1)))
        v1 = v[n-1].value
    return [i.value for i in v]


def xxtea_decrypt(n, v, key):
    # 全部转为c_unit32格式
    v = [c_uint32(i) for i in v]
    r = 6 + 52 // n
    v0 = v[0].value
    delta = 0x9e3779b9
    total = c_uint32(delta * r)
    for i in range(r):
        e = (total.value >> 2) & 3
        for j in range(n-1, 0, -1):
            v1 = v[j-1].value
            v[j].value -= ((((v1 >> 5) ^ (v0 << 2)) + ((v0 >> 3) ^ (v1 << 4))) ^ ((total.value ^ v0) + (key[(j & 3) ^ e] ^ v1)))
            v0 = v[j].value
        v1 = v[n-1].value
        v[0].value -= ((((v1 >> 5) ^ (v0 << 2)) + ((v0 >> 3) ^ (v1 << 4))) ^ ((total.value ^ v0) + (key[(0 & 3) ^ e] ^ v1)))
        v0 = v[0].value
        total.value -= delta
    return [i.value for i in v]



k = [0x5201314, 0x52013140, 0x5201314, 0x52013140]
v = [0x5A764F8A, 0x5B0DF77, 0xF101DF69, 0xF9C14EF4, 0x27F03590, 0x7DF3324F, 0x2E322D74, 0x8F2A09BC, 0xABE2A0D7, 0xC2A09FE, 0x35892BB2, 0x53ABBA12]

# 解密
for i in range(0, len(v), 2):
    v[i:i+2] = xxtea_decrypt(2, v[i:i+2], k)

# 输出解密后的数据
str_list = []
for i in range(len(v)):
    str_list.append(struct.pack('>I', v[i]).decode()[::-1])
print('decrypted: %s' % ''.join(str_list))


