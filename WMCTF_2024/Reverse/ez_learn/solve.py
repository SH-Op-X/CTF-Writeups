b = [214, 144, 233, 254, 204, 225, 61, 183, 22, 182, 20, 194, 40, 251, 44, 5, 43, 103, 154, 118, 42, 190, 4, 195, 170, 68, 19, 38, 73, 134, 6, 153, 156, 66, 80, 244, 145, 239, 152, 122, 51, 84, 11, 67, 237, 207, 172, 98, 228, 179, 28, 169, 201, 8, 232, 149, 128, 223, 148, 250, 117, 143, 63, 166, 71, 7, 167, 252, 243, 115, 23, 186, 131, 89, 60, 25, 230, 133, 79, 168, 104, 107, 129, 178, 113, 100, 218, 139, 248, 235, 15, 75, 112, 86, 157, 53, 30, 36, 14, 94, 99, 88, 209, 162, 37, 34, 124, 59, 1, 33, 120, 135, 212, 0, 70, 87, 159, 211, 39, 82, 76, 54, 2, 231, 160, 196, 200, 158, 234, 191, 138, 210, 64, 199, 56, 181, 163, 247, 242, 206, 249, 97, 21, 161, 224, 174, 93, 164, 155, 52, 26, 85, 173, 147, 50, 48, 245, 140, 177, 227, 29, 246, 226, 46, 130, 102, 202, 96, 192, 41, 35, 171, 13, 83, 78, 111, 213, 219, 55, 69, 222, 253, 142, 47, 3, 255, 106, 114, 109, 108, 91, 81, 141, 27, 175, 146, 187, 221, 188, 127, 17, 217, 92, 65, 31, 16, 90, 216, 10, 193, 49, 136, 165, 205, 123, 189, 45, 116, 208, 18, 184, 229, 180, 176, 137, 105, 151, 74, 12, 150, 119, 126, 101, 185, 241, 9, 197, 110, 198, 132, 24, 240, 125, 236, 58, 220, 77, 32, 121, 238, 95, 62, 215, 203, 57, 72]
s_init = [0x00022313, 0x00821DEF, 0x00123128, 0x43434310]
u1 = [0xA3B1BAC6, 0x56AA3350, 0x677D9197, 0xB27022DC]
u2 = [0x00070E15, 0x1C232A31, 0x383F464D, 0x545B6269, 0x70777E85, 0x8C939AA1, 0xA8AFB6BD, 0xC4CBD2D9, 0xE0E7EEF5, 0xFC030A11, 0x181F262D, 0x343B4249, 0x50575E65, 0x6C737A81, 0x888F969D, 0xA4ABB2B9, 0xC0C7CED5, 0xDCE3EAF1, 0xF8FF060D, 0x141B2229, 0x30373E45, 0x4C535A61, 0x686F767D, 0x848B9299, 0xA0A7AEB5, 0xBCC3CAD1, 0xD8DFE6ED, 0xF4FB0209, 0x10171E25, 0x2C333A41, 0x484F565D, 0x646B7279]
d1 = []
v = []
for i in range(4):
    v.append(s_init[i]^u1[i]^0x34343434)
for i in range(32):
    y = v[1]^v[2]^v[3]^u2[i]^0x12121212
    x = (b[(y>>24)&0xff]<<24)+(b[(y>>16)&0xff]<<16)+(b[(y>>8)&0xff]<<8)+(b[y&0xff])
    x = (((x<<23)|(x>>9))^((x<<13)|(x>>19))^x)&0xffffffff
    d1.append(v[0]^x^0x34343434)
    v.append(v[0]^x^0x34343434)
    v = v[1:]
str = [0xc676e86f, 0xad67e8f8, 0xca9db9ac, 0xb1ae068e, 0xd51b0298, 0xd827c6d3, 0x31a5a335, 0x893a7a66]
v = str[:4]
for i in range(31, -1, -1):
    y = v[1]^v[2]^v[3]^d1[i]^0x12121212
    x = (b[(y>>24)&0xff]<<24)+(b[(y>>16)&0xff]<<16)+(b[(y>>8)&0xff]<<8)+(b[y&0xff])
    x = (((x<<24)|(x>>8))^((x<<18)|(x>>14))^((x<<10)|(x>>22))^((x<<2)|(x>>30))^x)&0xffffffff
    v.append(v[0]^x^0x34343434)
    v = v[1:]
flag1 = b""
for i in v:
    flag1 += bytes.fromhex(hex(i)[2:])
v = str[4:]
for i in range(31, -1, -1):
    y = v[1]^v[2]^v[3]^d1[i]^0x12121212
    x = (b[(y>>24)&0xff]<<24)+(b[(y>>16)&0xff]<<16)+(b[(y>>8)&0xff]<<8)+(b[y&0xff])
    x = (((x<<24)|(x>>8))^((x<<18)|(x>>14))^((x<<10)|(x>>22))^((x<<2)|(x>>30))^x)&0xffffffff
    v.append(v[0]^x^0x34343434)
    v = v[1:]
flag2 = b""
for i in v:
    flag2 += bytes.fromhex(hex(i)[2:])
print(flag1[::-1]+flag2[::-1])
