out = [0xF6, 0xB0, 0xA6, 0x36, 0x9A, 0xB3, 0x2B, 0xBF, 0x94, 0x54, 0x15, 0x97, 0x93, 0x59, 0xBF, 0x50, 0x4D, 0xBF, 0x0A, 0x59, 0x06, 0xD7, 0x97, 0x50, 0xD6, 0x59, 0x54, 0xD7, 0xCF, 0x06, 0x5D, 0x20, 0x1D, 0x5A, 0x22, 0xEE, 0x99, 0x1F, 0xE1, 0x18]
print(len(out))
key = 'HelloSDS'
s = []
for i in range(256):
    s.append((i*167+173)%256)
print(s)
key_list = []
for i in range(8):
    key_list.append(ord(key[(i+3)%len(key)]) | (ord(key[(i+2)%len(key)])<<8) | (ord(key[(i+1)%len(key)])<<16) | (ord(key[(i)%len(key)])<<24))
print(key_list, len(key_list))
for i in range(7, -1, -1):
    tmp = out[39]
    for j in range(38, -1, -1):
        out[j+1] = out[j]
    out[0] = tmp
    for j in range(40):
        out[j] = s.index(out[j])
    out[0] ^= (key_list[i]&0xff)
    out[1] ^= ((key_list[i]>>8)&0xff)
    out[2] ^= ((key_list[i]>>16)&0xff)
    out[3] ^= ((key_list[i]>>24)&0xff)
    out[4] ^= (key_list[i]&0xff)
    out[5] ^= ((key_list[i]>>8)&0xff)
    out[6] ^= ((key_list[i]>>16)&0xff)
    out[7] ^= ((key_list[i]>>24)&0xff)
print("".join(map(chr, out)))