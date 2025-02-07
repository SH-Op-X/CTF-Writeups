s = "D2C22A62DEA62CCE9EFA0ECC86CE9AFA4ECC6EFAC6162C3636CC76E6A6BE"
for i in range(0, len(s), 2):
    n = int(s[i:i+2], 16)
    n = bin(n)[2:].zfill(8)[::-1]
    n = int(n, 2)
    print(chr(n), end="")