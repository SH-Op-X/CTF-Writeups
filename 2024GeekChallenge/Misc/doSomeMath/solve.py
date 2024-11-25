num = 99*100^60
print(bin(num))
n2 = "(().__ge__(())+().__ge__(()))"
l = []
while num:
    l.append(num % 2)
    num //= 2
s = ""
for i in range(len(l)):
    if l[i]:
        s += i * (n2 + "*")
        s = s[:-1] + "+"
print(s[:-1])
print(eval(s[:-1]))