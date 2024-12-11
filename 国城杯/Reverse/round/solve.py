key = b"c9m1bRmfY5Wk"
box = list(range(0x400))[::-1]
for i in range(0x400):
    box[i] ^= key[i%len(key)]

def add(box, c, v):
    v2 = ((c + box[v]) % 0x400 + 0x400) % 0x400
    return v2, (v + v2) % 0x400

def sub(box, c, v):
    v2 = ((c - box[v]) % 0x400 + 0x400) % 0x400
    return v2, (v + v2) % 0x400

def xor(box, c, v):
    v2 = ((c ^ box[v]) % 0x400 + 0x400) % 0x400
    return v2, (v + v2) % 0x400

def shl(c, v):
    v2 = (c >> 3) % 0x400
    return v2, (v + v2) % 0x400

def shr(c, v):
    v2 = (c << 3) % 0x400
    return v2, (v + v2) % 0x400


cmp = [0x160, 646, 0x2F0, 882, 65, 0, 0x7A, 0, 0, 7, 350, 360]
def recursive(v4, v):
    tmp = v4
    if len(v) == 12:
        print("".join(map(chr, v)))
        return
    for i in range(32, 127):
        c = i
        for j in range(32):
            v10 = ((box[v4]^c)%5+5)%5
            if v10 == 0:
                c, v4 = add(box, c, v4)
            elif v10 == 1:
                c, v4 = sub(box, c, v4)
            elif v10 == 2:
                c, v4 = xor(box, c, v4)
            elif v10 == 3:
                c, v4 = shl(c, v4)
            elif v10 == 4:
                c, v4 = shr(c, v4)
        if c == cmp[len(v)]:
            recursive(v4, v+[i])
        else:
            v4 = tmp

recursive(33, [])
# tmp = 33
# for k in range(len(cmp)):
#     for i in range(32, 127):
#         c = i
#         v4 = tmp
#         for j in range(32):
#             v10 = ((box[v4]^c)%5+5)%5
#             if v10 == 0:
#                 c, v4 = add(box, c, v4)
#             elif v10 == 1:
#                 c, v4 = sub(box, c, v4)
#             elif v10 == 2:
#                 c, v4 = xor(box, c, v4)
#             elif v10 == 3:
#                 c, v4 = shl(c, v4)
#             elif v10 == 4:
#                 c, v4 = shr(c, v4)
#         if c == cmp[k]:
#             print(k, chr(i))
#             if k in [0, 1, 2, 4, 6]:
#                 tmp = v4
#                 break
#             if k == 3 and i != ord("u"):
#                 continue
#             elif k == 3:
#                 tmp = v4
#                 break
#             if k == 5 and i != ord("D"):
#                 continue
#             elif k == 5:
#                 tmp = v4
#                 break
            # if k == 7 and i != ord("A"):
            #     continue
            # elif k == 7:
            #     tmp = v4
            #     break
            # if k == 8 and i != ord("N"):
            #     continue
            # elif k == 8:
            #     tmp = v4
            #     break
# D0g3xGC{round_and_rounD_we_go}