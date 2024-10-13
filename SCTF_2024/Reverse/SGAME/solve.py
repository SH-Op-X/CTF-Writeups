s = "^'''''''^''LLLLL''SS'''''''JJJJ'''VVV'''T''''''T''LLLLL"
print(len(s))
new_s = ""
for i in s:
    new_s += chr(ord(i)-7)
print(new_s)
print(bytes.fromhex("4C4C4C4C4C2727"))
s = "vw(vw(vw(4(|pqvs"
new_s = ""
for i in s:
    new_s += chr(ord(i)-8)
print(new_s)