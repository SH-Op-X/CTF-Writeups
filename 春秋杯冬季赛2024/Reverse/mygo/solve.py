from string import printable

qword = 0xCBF29CE484222325
s = "08985807b541d18fd5f2d079088c0b172282110ea367087223826d0a97ceea455feb92ec9da6ccc6418727fdc0a2295bbf325bb7f6fb98b90669076ed7c9bfb3d905a4abf3eb7f225f5741aae1954e6c8f70569021c638dde77f76949e5db63a7f98a3f5e1b1e3409b7cd1e5a8dea236d3c21142b990e7b8"

def brute(qword, i):
    q = qword
    for c1 in printable:
        for c2 in printable:
            q = qword
            q = 0x100000001B3 * (q ^ ord(c1)) & 0xffffffffffffffff
            q = 0x100000001B3 * (q ^ ord(c2)) & 0xffffffffffffffff
            if q == int(s[16*i:16*i+16], 16):
                return c1+c2, q

flag = ""
for i in range(15):
    f, qword = brute(qword, i)
    flag += f
print(flag)