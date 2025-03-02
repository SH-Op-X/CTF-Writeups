from z3 import *

rand_list = [12, 28, 11, 12, 14, 14]
s = Solver()
v = BitVec('v', 64)
for i in range(len(rand_list)):
    if rand_list[i] % 2:
        v = (v << rand_list[i] & 0xffffffff) ^ v
    else:
        v = (v >> rand_list[i] & 0xffffffff) ^ v
s.add(v==0xE4BE1307)
if s.check() == sat:
    ans = s.model()
    print(bin(ans[ans[0]].as_long())[2:].zfill(32))