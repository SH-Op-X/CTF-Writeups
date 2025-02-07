s = b"EBPGRM|VE9B]Q5Sb4vJ^2|ZoU[t?SiDf9Cx"
flag = "}"
for i in range(len(s)-2, -1, -1):
    flag += chr(s[i]^(ord(flag[-1])&0xf))
print(flag[::-1])