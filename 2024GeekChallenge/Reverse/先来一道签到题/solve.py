s = "TTDv^jrZu`Gg6tXfi+pZojpZSjXmbqbmt.&x"
print(len(s))
flag = ""
for i in range(len(s)):
    if i % 2:
        flag += chr(ord(s[i])+5)
    else:
        flag += chr(ord(s[i])^7)
print(flag)