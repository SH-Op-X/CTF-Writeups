# import random
# random.seed('D0_Y0u_Kn0w_Wh4t_th3_D0oR_Th1s_K3y_Op3ns?')
# flag=input().encode()
# a=random.randbytes(len(flag))
# d=(map(int.__lshift__,a,list.__mul__([4],len(flag))))
# e=map(int.__or__,d,map(int.__rshift__,a,list.__mul__([4],len(flag))))
# print(list(e))
# f=map(int.__or__,map(int.__lshift__,a,list.__mul__([4],len(flag))),e)
# print(list(f))
# g=map(int.__and__,f,list.__mul__([255],len(flag)))
# h=map(int.__xor__,flag,g)
# b = [235,128,107,33,10,206,158,151,158,88,130,190,155,207,94,28,65,9,102,5,241,184,74,129,3,46,216,20,112,95,201,86,215,220,220,7,45,81,145,229,152,241,4,135,16,118,102,144]
# i=map(int.__xor__,b,h)
# any(i)

import random
random.seed('D0_Y0u_Kn0w_Wh4t_th3_D0oR_Th1s_K3y_Op3ns?')
b = [235,128,107,33,10,206,158,151,158,88,130,190,155,207,94,28,65,9,102,5,241,184,74,129,3,46,216,20,112,95,201,86,215,220,220,7,45,81,145,229,152,241,4,135,16,118,102,144]
print(len(b))
a=random.randbytes(48)
d=(map(int.__lshift__,a,list.__mul__([4],48)))
e=map(int.__or__,d,map(int.__rshift__,a,list.__mul__([4],48)))
f=map(int.__or__,map(int.__lshift__,a,list.__mul__([4],48)),e)
g=map(int.__and__,f,list.__mul__([255],48))
h=list(g)
print(h,len(h))
flag=""
for i in range(48):
    flag+=chr(b[i]^h[i])
print(flag)