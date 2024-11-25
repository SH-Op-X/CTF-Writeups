s = 'zoXpih^lhX6soX7lr~DTHtGpX|'
print(len(s))
new_s = ""
# xor = [7, 7, 10, 7, 18, 62, 77, 7, 7, 7, 7, 0, 20, 17, 33, 51, 43, 3, 47, 7, 7, 7] + list(b"Y0S\t")
# print(len(xor))
for i in range(len(s)):
    new_s += chr((ord(s[i]) ^ 7))
table = "abcdefghijklmnopqrstuvwxyz"
c_table = "zvrnjfbywusqomkigecaxtplhd"
flag = ""
for i in range(26):
    flag += new_s[c_table.index(table[i])]
print(flag)