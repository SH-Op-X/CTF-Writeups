import struct
from ctypes import c_uint32


def tea_decrypt(r, v, key, delta):
    v0, v1 = c_uint32(v[0]), c_uint32(v[1])
    total = c_uint32(delta * r)
    for i in range(r):
        v1.value -= ((v0.value << 4) + key[2]) ^ (v0.value + total.value) ^ ((v0.value >> 5) + key[3])
        v0.value -= ((v1.value << 4) + key[0]) ^ (v1.value + total.value) ^ ((v1.value >> 5) + key[1])
        total.value -= delta
    return v0.value, v1.value


def rol(v, r):
    return (v << r | v >> (32 - r)) & 0xffffffff


if __name__ == "__main__":
    k = [0x56789ABC, 0x6789ABCD, 0x789ABCDE, 0x89ABCDEF]
    v = [0x1F85A965, 0xEEC063EC, 0x5BF1D0B6, 0xF2FDE7B0, 0xAA38809A, 0x670772E9, 0x360D24B9, 0xE98C688C]
    for i in range(0, len(v), 2):
        k[i // 2] = rol(k[i // 2], 6)
        delta = ((k[0] ^ k[1])&0xff) - 0x6789ABCE
        v[i:i+2] = tea_decrypt(32, v[i:i+2], k, delta)
    str_list = []
    for i in range(len(v)):
        str_list.append(struct.pack('<I', v[i]).decode())
    print('decrypted: %s' % ''.join(str_list))
