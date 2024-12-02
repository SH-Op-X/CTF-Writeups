import struct
from ctypes import c_uint32

s = [0x000000A5, 0x00000064, 0x0000009F, 0x00000004, 0x00000039, 0x000000B7, 0x000000A6, 0x00000017, 0x00000022, 0x000000CD, 0x00000026, 0x0000004D, 0x0000007D, 0x00000010, 0x00000082, 0x000000DB, 0x00000085, 0x000000DB, 0x00000027, 0x00000039, 0x00000042, 0x0000003C, 0x0000001E, 0x000000A5, 0x00000022, 0x000000CD, 0x00000026, 0x0000004D, 0x0000007D, 0x00000010, 0x00000082, 0x000000DB, 0x000000D6, 0x00000037, 0x00000068, 0x00000080, 0x000000B1, 0x000000F9, 0x00000015, 0x00000019, 0x00000044, 0x00000018, 0x00000042, 0x00000024, 0x0000008F, 0x00000078, 0x000000A2, 0x0000002C]
v = []
for i in range(0, len(s), 4):
    # v.append(s[i]+(s[i+1]<<8)+(s[i+2]<<16)+(s[i+3]<<24))
    v.append(s[i+3]+(s[i+2]<<8)+(s[i+1]<<16)+(s[i]<<24))
print(list(map(hex, v)))

def tea_encrypt(r, v, key, delta):
    v0, v1 = c_uint32(v[0]), c_uint32(v[1])
    total = c_uint32(0xC6EF3720)
    for i in range(r):
        v1.value -= ((v0.value << 4) + key[2]) ^ (v0.value + total.value) ^ ((v0.value >> 5) + key[3])
        v0.value -= ((v1.value << 4) + key[0]) ^ (v1.value + total.value) ^ ((v1.value >> 5) + key[1])
        total.value += delta
    return v0.value, v1.value

def tea_decrypt(r, v, key, delta):
    v0, v1 = c_uint32(v[0]), c_uint32(v[1])
    total = c_uint32(0xC6EF3720+delta * r)
    for i in range(r):
        total.value -= delta
        v0.value += ((v1.value << 4) + key[0]) ^ (v1.value + total.value) ^ ((v1.value >> 5) + key[1])
        v1.value += ((v0.value << 4) + key[2]) ^ (v0.value + total.value) ^ ((v0.value >> 5) + key[3])
    return v0.value, v1.value

k = [0x0000004C, 0x0000005A, 0x00000053, 0x00000044]
for i in range(len(v)):
    v[i] ^= 0x53
delta = 0x61C88647
for i in range(0, len(v), 2):
    v[i:i+2] = tea_decrypt(32, v[i:i+2], k, delta)
print(list(map(hex, v)))
str_list = []
for i in range(len(v)):
    str_list.append(struct.pack('<I', v[i]).decode())
print('decrypted: %s' % ''.join(str_list))
out = ''.join([i[0]+i[2]+i[1] for i in str_list])
print(out)
table = "hijklmnopqrstuvwxyz0123456BCDEFGHIJKLMNOPQRSTUVWXYZawxyz01234579f!"
tabl1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_!'
flag = ""
for i in range(len(out)):
    try:
        flag += tabl1[table.index(out[i])]
    except:
        flag += " "
print(flag)
