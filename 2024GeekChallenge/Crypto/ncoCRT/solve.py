from Cryptodome.Util.number import long_to_bytes

p = [1921232050179818686537976490035, 2050175089402111328155892746480, 1960810970476421389691930930824, 1797713136323968089432024221276, 2326915607951286191807212748022]
c = [1259284928311091851012441581576, 1501691203352712190922548476321, 1660842626322200346728249202857, 657314037433265072289232145909, 2056630082529583499248887436721]
n = 5  # 同余方程个数

"""扩展欧几里得"""


def exgcd(a, b):
    if 0 == b:
        return 1, 0, a
    x, y, q = exgcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q


"""扩展中国剩余定理"""


def CRT():
    if n == 1:
        if p[0] > c[0]:
            return c[0]
        else:
            return -1

    for i in range(n):
        if p[i] <= c[i]:
            return -1

        x, y, d = exgcd(p[0], p[i])
        if (c[i] - c[0]) % d != 0:
            return -1

        t = p[i] // d
        x = (c[i] - c[0]) // d * x % t
        c[0] = x * p[0] + c[0]
        p[0] = p[0] * p[i] // d
        c[0] = (c[0] % p[0] + p[0]) % p[0]

    return c[0]


ans = CRT()
print(long_to_bytes(ans)[:-23].decode())
