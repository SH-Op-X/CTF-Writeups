s = [108, 198, 100, 160, 178, 144, 242, 166, 232, 240, 232, 220, 114, 228, 152, 152, 242, 242, 170, 210, 226, 138, 210, 130, 160, 170, 202, 112, 202, 176, 212, 196, 174, 156, 170, 222, 212, 142, 208, 198, 112, 214, 152, 170]
print(len(s))
for i in range(len(s)):
    s[i] //= 2
print("".join(map(chr, s)))