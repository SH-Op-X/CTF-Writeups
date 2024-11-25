import base64

from Crypto.Util.number import bytes_to_long

correct_table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'
table = 'eM+wr=x8aYZ/[zU$yRB&kbO;%p0P5f*7d(n]1Eug4ojc62AC,v39!h-^qQ.G?s)i:DFlS<>#@HINJTmtKLVWX'
c = 'RjB6Myu#,>Bgoq&u.H(nBgdIaOKJbgEYj1GR4S.w'
new_c = []
for i in range(len(c)):
    new_c.append(correct_table[table.index(c[i])])
base85_c = base64.b85decode(''.join(new_c))
print(base85_c) # 6pmB34FC9sbYxcKP9rjGGiyRsx1s6c72

b58_list = ["K75qMosjadPUyGNmtT6bCzLvW4wXhpgc1Dx2iukS38JVHR9EFZArQnYefB",
"TfRCQJ85UVHtM1AuDFmiErXYwy63qgSnKbeWxpjBosZ79zavG4cN2PLhdk",
"ZGkXUoSQKvmj46VgyPwtaeJzcLY1pu52RFB8d3EDrh9HCbAfiq7nTNWMsx",
"hp8uXLiCJaTk7SzvxYEZGMHsBwP9c3dF5qVeQU2ytbRrfgDnW6A4Noj1Km",
"oQTGZpx43AD8VsRbkUXhamdnu9vwEWfySL6MJ7K2jYg15cqtrCezFNPHiB",
"txodKFNw4spbmgeMnrBzRLZvjkQ3EXSUuTA9YJi561aPCHfc82qVhGWDy7",
"2Y9zgpXjnxWFahSZfG315LkvtyoNs8KRd6bTeQBHEcuDAr4CP7UVmiwJMq",
"86ULkMn3fs9ASdJbyRjDBzghcuVQTFxpo5YEN4rm1CqiHWXaPZt27wevKG",
"Ggrhn5MYjos1zVTFi4ZaQ2Dt3p8XAUbWyRBJSkwuedmfqc96xLPNKEHC7v",
"NFB4qMLhQdSXJPiz7CypVrubEgvc6k9Z85R3jtAHoUa1nY2wDmefxWKGTs",
"UqXRutc2H6DimQJzgr5eEjaT9fnh1BypxLwGokv8KFYbNP7A4CSVdsW3ZM",
"cPsnwuN8j9C1rxBmoLe5Z4vVkHEQFYfK2RXWAtp7qJDG6zU3aibSTgydMh",
"iyC8ztAg1JNbaXpWfedxZ4UuHLqrTMjhD56QEF37vP9w2YKnsmSoGBVkcR",
"rXaV4RzuC2GY9Zt7qWpTJv56nSidQUcmBP3MeA8oNkyjLgH1EDhfFxbsKw",
"x7urvjMk6fRGEXTeS94ALVstzhwn1UFCQPocHJgmqW3yid5BZN8YapKDb2",
"4fFDBRzdxKcreq3HA8MQLXPWuynUhbJE51s6VN7ZvwtCS9agGmYk2jiTop",
"CDbawF1VrxJG2ejY9EcfZsLuXR8hSTBAUi7kQoPNWM4n5qKg6mvpdt3yHz",
"JpvGSYKNmbzhQd41F79Dj8CWk5ufeVMT6sBgqUwtayxH3oiZnPr2RLAXcE",
"QNJHLwpeDfF8n5Ztb2Bu4aGg3M6RrvcqY7TXzmhWxoACKjski1y9VUSdPE",
"YxdeNU5z6XtMAoS4kwVHyvDETJjuBGQRcmngiP37rCabpqFL8Z1shfW92K",
"eWy1RNJzY3VLacpkDPGCvrEhSQunmKoAt4wjix8UB76MTqsgZ5XFd9fbH2",
"n6KPVUdeqBjQvDG51Nof9uJHW7gRAtLrCcTkXhz2ips3Sb8yFmYa4xZMEw",
"tegkX1wyiCpNqJuAbMacG3D6nv2H78ShYK4RmVdzUjWZBoLsETP9fFQxr5",
"zE25aWCHZ6U4FgdBXGMPv7oAi8pjTK3kDQNe1brfVhwSRnsYtuqLcyJmx9",
"8oMSe1Tdz7kg4Kyc3ZQnsYi2u6btjxLPqrJFHXVmDRaAvEB9GWCwUphf5N",
"EPhoYkwLtmS73svK241dcyNpReZTAgDW69JMqQuFn5BVjxXfUbCr8GaHiz",
"Nw3Bm2JkQ8XpjenYCAryEvDz9VuosGM4dTFH5iZxqUWRfc61PShatbgKL7",
"TXQYoHc4fxCh8e27bKGmvpuytka9AZFSnW6LqisJVjPzgBEdR35MwNDr1U",
"Z5ksr2avhVP9bfWpUXg7uTKE6NmCxnQG3dMDYSBzAiqFjwRtHoyL4J1ce8",
"hf5EvZqGoTL9xsVPt1u7dm8r4gbkCRSzHMpUwJ6e2NQijYKWnAcXBayD3F"
            ]
for base58_alphabet in b58_list:

    def custom_base58_encode(input_string):
        # 初始化字符表

        # 计算输出缓冲区大小 `v7`
        v7 = 138 * len(input_string) // 100 + 1

        # 初始化 Block 和 v5，模拟 C 代码中的 malloc
        block = [0] * v7
        encoded_result = [""] * v7

        # `v10` 用于遍历 input_string，`v8` 为 encoded_result 的索引
        v10 = 0

        while v10 < len(input_string):
            v9 = ord(input_string[v10])  # 当前字符的 ASCII 值
            # 类似于进制转换，将每个字符映射到 Base58 字符集中
            for i in range(v7 - 1, -1, -1):
                v9 += block[i] << 8  # 左移以累加 ASCII 值
                block[i] = v9 % 58  # 取余以限制在 Base58 范围内
                v9 //= 58  # 整除以进行进位
                if v9 == 0:
                    break
            v10 += 1
        # print(block)
        # 处理前导零
        i = 0
        while i < v7 and block[i] == 0:
            i += 1

        # 将编码结果填充到 encoded_result 中
        v8 = 0
        while i < v7:
            encoded_result[v8] = base58_alphabet[block[i]]
            v8 += 1
            i += 1

        # 组合成最终字符串，模拟 C 中的 null-terminated 字符串
        return ''.join(encoded_result[:v8])


    def custom_base58_decode(encoded_string):
        # Initialize character table
        base58_map = {char: idx for idx, char in enumerate(base58_alphabet)}

        # Initialize block size based on the encoded string length
        block_size = 100

        # Initialize block array and result array
        block = [0] * block_size

        for char in encoded_string:
            value = base58_map[char]  # Get index of character in base58_alphabet
            for i in range(block_size - 1, -1, -1):
                value += block[i] * 58  # Scale up by 58 for the reverse of modulo
                block[i] = value % 256  # Take modulo 256 for byte value
                value //= 256  # Move to next byte
            if value != 0:
                raise ValueError("Base58 decoding error: non-zero value remains.")

        # Skip leading zeroes
        i = 0
        while i < len(block) and block[i] == 0:
            i += 1

        # Convert decoded bytes into characters
        decoded_result = ''.join(chr(b) for b in block[i:])

        return decoded_result

    print(custom_base58_decode("6pmB34FC9sbYxcKP9rjGGiyRsx1s6c72"))
