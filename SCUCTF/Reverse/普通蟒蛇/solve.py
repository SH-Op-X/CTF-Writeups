flag = "SCUCTF{%s}"
s = [61, 99, 197, 227, 156, 68, 143, 194, 241, 148, 138, 234, 254, 201, 60, 22, 230]
# for i in range(256):
#     new_s = s
#     for j in range(len(s)):
#         new_s[j] ^= i
#     print("".join(map(chr, new_s)))
# flag = ""
# for i in range(len(s)):
#     if ((s[i] + 8) + 171) & 0x10 == 0:
#         flag += chr(s[i])
#     else:
#         if ((s[i] + 16) + 171) & 0x10 == 0: