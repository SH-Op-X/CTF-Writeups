key = 'REVOLCYS'[::-1]
data = [0, 1, 2, 52, 3, 96, 47, 28, 107, 15, 9, 24, 45, 62, 60, 2, 17, 123, 39, 58, 41, 48, 96, 26, 8, 52, 63, 100, 33, 106, 122, 48]
flag = ""
for i in range(len(data)):
    flag += chr(i ^ data[i] ^ ord(key[i%8]))
print(flag)