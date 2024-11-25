from z3 import sat, Int, Solver

s = Solver()
data = [0x0000019B, 0x00000113, 0x00000189, 0x000001C9, 0x00000250, 0x00000536, 0x000004DE, 0x000001BC, 0x0000041B, 0x00000724, 0x000006D0, 0x000004A1, 0x00000645, 0x00000475, 0x000004CA, 0x0000068C, 0x000003E5, 0x000001C7, 0x0000033D, 0x000005B7, 0x0000028D, 0x00000244, 0x0000030E, 0x00000291, 0x00000271, 0x00000301, 0x0000045F, 0x0000046F, 0x00000517, 0x0000041E, 0x00000426, 0x000004B5]
a = [Int(f"a{i}") for i in range(32)]
for i in range(0, 32, 4):
    s.add(a[i]+8*a[i+1]+6*a[i+2]+a[i+3]==data[i])
    s.add(a[i+1]+8*a[i+2]+6*a[i+3]+a[i]==data[i+1])
    s.add(a[i+2]+8*a[i+3]+6*a[i]+a[i+1]==data[i+2])
    s.add(a[i+3]+8*a[i]+6*a[i+1]+a[i+2]==data[i+3])
idx = [0x2A, 0x0E, 0x0E, 0x14, 0x3F, 0x3F, 0x3F, 0x26, 0x11, 0x0A, 0x15, 0x15, 0x0E, 0x17, 0x10, 0x0E]
table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?_'
s1 = [ord(table[idx[i]]) for i in range(len(idx))]
print(len(s1), s1, "".join(map(chr, s1)))
if s.check() == sat:
    ans = s.model()
    print(ans)
    flag = []
    for i in range(len(a)):
        flag.append(ans[a[i]].as_long())
    print(list(map(hex, flag)))
    for i in range(len(flag)-1, -1, -1):
        flag[i] ^= (s1[(47-i)%16]^i)
        flag[i] ^= flag[i-1]
    flag = "".join(map(chr, flag))
    print(flag)
    for i in range(0, 32, 4):
        print(flag[i+(i//4*3%4):i+4]+flag[i:i+(i//4*3%4)], end="")
