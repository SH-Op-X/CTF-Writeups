from gmpy2 import invert
cmp = [0x12287f38, 0x98d24b3a, 0x4a30f74d, 0xe0f1db77, 0x23a1268, 0xadf38403, 0x88108807, 0xd8499bb6]
flag = ""
for i in range(0, 8, 2):
    # 第一部分
    c = cmp[i+1]
    p = 9241
    q = 464773
    phi = (p-1) * (q-1)
    d = invert(65537, phi)
    m1 = pow(c, d, 0xfffffffd)
    m1 <<= 11
    m1 ^= 0x9e3779b9
    m1 >>= 11
    # 第二部分
    assert m1 >> 17 == cmp[i] & 0xf
    m2 = (cmp[i]>>4) & (2**11-1)
    m = (m1 << 11) + m2
    flag += hex(m)[2:].zfill(8)
print(f"flag{{{flag}}}")