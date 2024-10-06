from hashlib import sha256

s = '{a67be199da4b-b092-bd3e-e777-a67be199da4b}'
hash = sha256(s.encode()).hexdigest()
lens = [8, 4, 4, 4, 12]
flag = "ByteCTF{"
k = 1
for i in range(len(lens)):
    flag += hash[k:k+lens[i]].replace(chr(97+i), chr(97+i+1))
    k = 1 + lens[i]
    if i!=len(lens)-1:
        flag += "-"
flag += "}"
print(flag)
