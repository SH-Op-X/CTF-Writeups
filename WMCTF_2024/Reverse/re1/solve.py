import struct
from ctypes import c_uint32


def xtea_decrypt(r, v, key):
    v0, v1 = c_uint32(v[0]), c_uint32(v[1])
    delta = 0x5EEFEF3
    total = c_uint32(-delta * r)
    for i in range(r):
        v1.value -= (((v0.value << 6) ^ (v0.value >> 6)) + v0.value) ^ (total.value + key[(total.value & 0xff) >> 6])
        total.value += delta
        v0.value -= (((v1.value << 6) ^ (v1.value >> 6)) + v1.value) ^ (total.value + key[total.value & 3])
    return v0.value, v1.value

out = [0xEFC05FD2, 0x9378625E, 0x841F41A0, 0x06D05F4A, 0xDC898F9A, 0x21AA7CFC, 0x4229FB0B, 0x31E52B8B]
key = [0xFFFFFFFF, 0xAAAAAAAA, 0x11111111, 0x11111111]
for i in range(0, len(out), 2):
    out[i:i + 2] = xtea_decrypt(66, out[i:i + 2], key)
str_list = []
for i in range(len(out)):
    str_list.append(struct.pack('<I', out[i]))
flag = ""
str_list = b"".join(str_list)
for i in range(len(str_list)):
    flag += chr(i ^ 0x5a ^ str_list[i])
print(flag)