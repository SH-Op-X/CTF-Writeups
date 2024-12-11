cmp = [214, 144, 233, 254, 204, 225, 61, 183, 22, 182, 20, 194, 40, 251, 44, 5, 43, 103, 154, 118, 42, 190, 4, 195, 170, 68, 19, 38, 73, 134, 6, 153, 156, 66, 80, 244, 145, 239, 152, 122, 51, 84, 11, 67, 237, 207, 172, 98, 228, 179, 28, 169, 201, 8, 232, 149, 128, 223, 148, 250, 117, 143, 63, 166, 71, 7, 167, 252, 243, 115, 23, 186, 131, 89, 60, 25, 230, 133, 79, 168, 104, 107, 129, 178, 113, 100, 218, 139, 248, 235, 15, 75, 112, 86, 157, 53, 30, 36, 14, 94, 99, 88, 209, 162, 37, 34, 124, 59, 1, 33, 120, 135, 212, 0, 70, 87, 159, 211, 39, 82, 76, 54, 2, 231, 160, 196, 200, 158, 234, 191, 138, 210, 64, 199, 56, 181, 163, 247, 242, 206, 249, 97, 21, 161, 224, 174, 93, 164, 155, 52, 26, 85, 173, 147, 50, 48, 245, 140, 177, 227, 29, 246, 226, 46, 130, 102, 202, 96, 192, 41, 35, 171, 13, 83, 78, 111, 213, 219, 55, 69, 222, 253, 142, 47, 3, 255, 106, 114, 109, 108, 91, 81, 141, 27, 175, 146, 187, 221, 188, 127, 17, 217, 92, 65, 31, 16, 90, 216, 10, 193, 49, 136, 165, 205, 123, 189, 45, 116, 208, 18, 184, 229, 180, 176, 137, 105, 151, 74, 12, 150, 119, 126, 101, 185, 241, 9, 197, 110, 198, 132, 24, 240, 125, 236, 58, 220, 77, 32, 121, 238, 95, 62, 215, 203, 57, 72, 85, 208, 152, 146, 101, 178, 190, 37, 195, 193, 121, 4, 181, 209, 153, 206]
print(len(cmp))
def hh(a0, a1):
    return (a0 << a1) | (a0 >> (32 - a1))

def ii(a):
    return cmp[((a >> 4) * 16) + (a & 15)]

def jj(a):
    obj = 0
    for i in range(3, -1, -1):
        if obj:
            obj += obj << 8
        obj += ii((a >> (i * 8)) & 255)
    return obj

def kk(a):
    obj = 0
    for i in range(4):
        if obj:
            obj += 1
        obj += a[i] << (8 * (3 - i))
    return obj

def mm():
    newobjrange = [0] * 36
    for i in range(4):
        newobjrange[i] = kk(cmp[i*4:i*4+4])
    for i2 in range(32):
        newobjrange[i2 + 4] = (newobjrange[i2 + 1] ^ newobjrange[i2 + 2]) ^ newobjrange[i2 + 3]
        newobjrange[i2 + 4] = jj(newobjrange[i2 + 4])
        newobjrange[i2 + 4] = (newobjrange[i2 + 4] ^ hh(newobjrange[i2 + 4], 13)) ^ hh(newobjrange[i2 + 4], 23)
        newobjrange[i2 + 4] = newobjrange[i2 + 4] ^ newobjrange[i2]
    return newobjrange[4:36]

def ll(a):
    j = jj(a)
    return (((j ^ hh(j, 2)) ^ hh(j, 10)) ^ hh(j, 18)) ^ hh(j, 24)

def gg(s):
    m = mm()
    print(m)
    newobjrange2 = [0] * 36
    for i in range(4):
        newobjrange2[i] = kk(s[i * 4:i * 4 + 4])
    for i2 in range(32):
        newobjrange2[i2 + 4] = ((newobjrange2[i2 + 1] ^ newobjrange2[i2 + 2]) ^ newobjrange2[i2 + 3]) ^ m[i2]
        newobjrange2[i2 + 4] = ll(newobjrange2[i2 + 4])
        newobjrange2[i2 + 4] = newobjrange2[i2 + 4] ^ newobjrange2[i2]
    for i3 in range(4):
        s[4 * i3] = (newobjrange2[35 - i3] >> 24) & 255
        s[(4 * i3) + 1] = (newobjrange2[35 - i3] >> 16) & 255
        s[(4 * i3) + 2] = (newobjrange2[35 - i3] >> 8) & 255
        s[(4 * i3) + 3] = newobjrange2[35 - i3] & 255
    return s


result = gg([0]*16)
print(result)
print(cmp[256:], len(cmp[256:]))
compare = []
for i in range(16):
    compare.append(cmp[cmp[256+i]])
print(bytes(compare).hex())
print(bytes(cmp[:16]).hex())
print(gg(compare))
