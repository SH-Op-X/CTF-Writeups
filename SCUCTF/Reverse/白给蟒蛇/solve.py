cmp = [
 18, 19, 42, 84, 75, 113, 53, 42, 60, 98, 109, 126, 73, 42, 21, 44,
 82, 54, 84, 32, 140, 48, 101, 218, 92, 83, 210, 55, 51, 160, 148,
 129, 253]
flag = ""
for i in range(len(cmp)-1, -1, -1):
    cmp[i] -= i
    cmp[i] ^= cmp[(i - 3 + 33) % 33]
print("".join(map(chr, cmp)))
