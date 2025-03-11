from base64 import b64decode, b64encode


def KSA(key):
    """ Key-Scheduling Algorithm (KSA) 密钥调度算法"""
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S):
    """ Pseudo-Random Generation Algorithm (PRGA) 伪随机数生成算法"""
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key, text):
    """ RC4 encryption/decryption """
    S = KSA(key)
    keystream = PRGA(S)
    res = []
    for char in text:
        res.append((((char- 57)&0xff) ^ next(keystream)))
    return bytes(res)

def case1(a, b):
    original_a1 = []
    for i in range(len(a)):
        c = a[i]
        v22 = b[i % len(b)]
        if 65 <= c <= 90:  # 大写字母
            x = (c - 65 - v22 + 26) % 26 + 65
            original_a1.append(chr(x))
        elif 97 <= c <= 122:  # 小写字母
            x = (c - 97 - v22 + 26) % 26 + 97
            original_a1.append(chr(x))
        elif 48 <= c <= 57:  # 数字
            x = (c - 48 - v22 + 10) % 10 + 48
            original_a1.append(chr(x))
        else:  # 非字母数字字符
            original_a1.append(chr(c))

    return ''.join(original_a1).encode()


def case3(a, b):
    # 计算分块的行数
    rows = b[0] % 10 + 2
    # 计算分块的列数
    if len(a) % rows:
        cols = len(a) // rows + 1
    else:
        cols = len(a) // rows

    # 初始化一个二维数组 Block
    Block = [[None for _ in range(cols)] for _ in range(rows)]

    # 将 encoded_str 按行优先填充到 Block 中
    index = 0
    if len(a) % rows:
        for i in range(rows):
            for j in range(cols):
                if index < len(a):
                    if i >= len(a) % rows and j == cols - 1:
                        Block[i][j] = None
                    else:
                        Block[i][j] = a[index]
                        index += 1
                else:
                    Block[i][j] = None  # 填充空值
    else:
        for i in range(rows):
            for j in range(cols):
                if index < len(a):
                    Block[i][j] = a[index]
                    index += 1
                else:
                    Block[i][j] = None  # 填充空值

    # 按列优先读取 Block，还原原始字符串
    original_str = []
    for j in range(cols):
        for i in range(rows):
            if Block[i][j] is not None:
                original_str.append(Block[i][j])

    # 将列表转换为字符串
    return ''.join(map(chr, original_str)).encode()


def case4(a, b):
    k = b[0] % 10 + 2
    return a[k:] + a[:k]

def mybase64(c):
    c = c.decode()
    correct_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    table = 'stuvwxyz0123456789+/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr'
    new_c = []
    for i in range(len(c)):
        if c[i] != '=':
            new_c.append(correct_table[table.index(c[i])])
        else:
            new_c.append(c[i])
    return list(b64decode(''.join(new_c)))

def mybase641(c):
    c = b64encode(c)
    correct_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    table = 'stuvwxyz0123456789+/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr'
    new_c = []
    for i in range(len(c)):
        if chr(c[i]) != '=':
            new_c.append(table[correct_table.index(chr(c[i]))])
        else:
            new_c.append(chr(c[i]))
    return ''.join(new_c).encode()

def case5(a, b):
    a = mybase64(a)
    for i in range(len(a)):
        a[i] ^= (b[i%len(b)] + 57)
    return bytes(a)

def case6(a, b):
    a = mybase64(a)
    return RC4(b, a)

print(case1(bytes.fromhex("757575757575757575757575"), bytes.fromhex("626262626262626262626262")).hex())
print(case5(bytes.fromhex("6e616e616e616e616e616e616e616e61"), bytes.fromhex("626262626262626262626262")).hex())
print(case1(bytes.fromhex("777777777777777777777777"), bytes.fromhex("636363636363636363636363")).hex())
print(case6(bytes.fromhex("584b31396d6546632f586d79636b5758416d785970733d3d"), bytes.fromhex("777777777777777777777777")).hex())
print(case5(bytes.fromhex("6d7162586d7162586d7162586d716258"), bytes.fromhex("636363636363636363636363")).hex())
print(case1(bytes.fromhex("777777777777777777777777"), bytes.fromhex("636363636363636363636363")).hex())
print(case3(bytes.fromhex("58793d4b633d316b39576d586541466d63782f5958706d73"), bytes.fromhex("6d7162586d7162586d7162586d716258")).hex())
print(case6(bytes.fromhex("495a7668694451774a6c7362334a76643731314a7a733d3d"), bytes.fromhex("6d7a7a68687a7578786d6874")).hex())
print(case4(bytes.fromhex("5958706d7358793d4b633d316b39576d586541466d63782f"), bytes.fromhex("495a7668694451774a6c7362334a76643731314a7a733d3d")).hex())

str1 = b"WgvDmssEvcY326bHo3nNro3vXvvfmgrz"
str2 = b"gX+Ri9PG=bt5=00B6hscPQOL"
str3 = b"T6bHgUPL2gXUd=xT=FNHtPzV"
str3 = case1(str3, str1)
str2 = case4(str2, str3)
str1 = case5(str1, str2)
str3 = case4(str3, str1)
str2 = case1(str2, str3)
str1 = case4(str1, str2)
str3 = case3(str3, str1)
str2 = case4(str2, str3)
str1 = case1(str1, str2)
str3 = case6(str3, str1)
str2 = case3(str2, str3)
str1 = case4(str1, str2)
str3 = case5(str3, str1)
str2 = case6(str2, str3)
str1 = case3(str1, str2)
str3 = case1(str3, str1)
str2 = case5(str2, str3)
str1 = case6(str1, str2)
str2 = case1(str2, str3)
str1 = case5(str1, str2)
str1 = case1(str1, str2)
print(str1+str2+str3)