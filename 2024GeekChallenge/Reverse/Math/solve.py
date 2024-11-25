import base64

from Crypto.Util.number import long_to_bytes
from sympy import discrete_log, factor
from sympy.ntheory.modular import crt

correct_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
table = 'CDEqrIJKNOPABdefghijklmQRSTstuvwxyz01VWXYZabcnop456L23FGHUM789+/'


c = 'd0BURFg2dLNFBLDySWN5RmrUS0k2ejDzdJRLSJkLR0gGBqIVSmR3RLR5RmI1BqRLdqlWemk4Bqr4B0rLdqD0S01HemS0Bqx6d01LS0t2djt5dWO1BLV1Bqr3dL1LSjR6RWk4eq15BFh0R0x6R0OzdWBHSmg3dWg5dmr2RFB6BLDyd0DVRjrHdmg3ejdyeqkHR0gGB0tFRLg4BFBGemNFSJr6BFN3d0IzB0C4B013RjyySJhzRjuydqxFd0D1BjuyemlVS0B6BWk2BLDzejBURml0RLh0RjD0BJR2SWd0BqCLdjN2RFh0RjRHR0uzSj1Ldj1FBWR2R0hySqy0RmS1dg=='
new_c = []
for i in range(len(c)):
    if c[i] != '=':
        new_c.append(correct_table[table.index(c[i])])
    else:
        new_c.append(c[i])
cc = int(base64.b64decode(''.join(new_c)).decode(), 16)
print("c: ", cc)

c = 'BjI1S0t5djR4dj14dWBURFS0ejCFSWIWdJg4BWrLeqDzejgHemSVeq14ejk6RFSzRLtGBjdyS0xGBqB5R0R5RjhyBFr4SjO0dqSzRjxUSmR2d0OyBFrGdFhVS0u1dmhVBJr4Rjr4R0d1BjB4BFIWRLCFSmgGRWBUS0CGSjC5Sj1HeqdzBqS0SjrGRLNUBJSVdjk4eqg2RFRUBqNHS0k4d0g6Sjg5ejD0RFN5BFd1S0DzR0C2ejdVdqBGRLk2Smk5dLR2BLN4BWd0BmNLdjt2BjN4eq13dFlzdWB5eqgLB01UR0g2eqDVdWgLBWrLBjI1SjSWSqSWdJNUSqVVeJSyRx=='
new_c = []
for i in range(len(c)):
    if c[i] != '=':
        new_c.append(correct_table[table.index(c[i])])
    else:
        new_c.append(c[i])
n1 = int(base64.b64decode(''.join(new_c)).decode(), 16)
print("n1: ", n1)

c = 'dmrGd0yVeJkLSjhVSWk3BmR3d0S1dLu1SqVyBjB5BWR3BL1HRWBUSjIWRjhVeqNHRWkFRjdzdWIyd0r4emhVBqO0dJlVRLk6dJk6BFOWBqxLdWNGR0N3S0kLdJr2B01GdqhVejx4RWh0BFI0SqtGRjx5BLd0djgLSmr5RFR2S0gFd0lWRWg2dWO0B0I1BLyVSJgFBJrFeqt4BquVBqtUejx4RFI0ejuVBjCUejR5BJIVRFlVSjdzSWR5BLgHBLBUdWr2RFSzBqR5SJRGSqlzRFkURLuWRWrFRmk5dJSzSmI1dmR3dWIyej14S0NLSmkURFOVeJrHSWB4d0S1dmSy'
new_c = []
for i in range(len(c)):
    if c[i] != '=':
        new_c.append(correct_table[table.index(c[i])])
    else:
        new_c.append(c[i])
c1 = int(base64.b64decode(''.join(new_c)).decode(), 16)
print("c1: ", c1)

c = 'RLdWSqx2RWlVR0NLd0d1dqr2eqgHSWhydjxUeq1Gd0R6dmO0RWNUd0BGejx6S0xLeqkLRjS0ejSVd0h0eJl0ejgFdqk2BqVzdLCLdWkLR0rHdFl0S01LBJk6ejhWRLg2eJB2RmBFRWSyej12djCGeqB4BJN5d0rURWBUeJg5BLNGdjtGBJR3d0NHdLh0dFS1BLxURWrUSmR2SjC3BqrUd0BLdjRFSjR3RWrUdmk3RjB4SjNURjg3R0tUdLt2RLSyRml1eqVyRjgLBjC3djCHSjxFeq12BmBHBjxFBjr6BJR3BJSVBjx6SjBLR0x4dLC5SjrGBjg6BqkGdjVWBLx4'
new_c = []
for i in range(len(c)):
    if c[i] != '=':
        new_c.append(correct_table[table.index(c[i])])
    else:
        new_c.append(c[i])
hint1 = int(base64.b64decode(''.join(new_c)).decode(), 16)
print("hint1: ", hint1)

c = 'BFd0BqCFSjD1Smr4dFRHBLg2Bjx5BqVyRLy0Bmr2dqt6djy0dFhyBqr6B0B5BquWSqN3djB4BLR5BFdVemSWRLdWRmrGdqx6BFr6eJlyBmk6BjIyBLh0BLgUS0N4R0gURWN4Bqg2dLtGdFk2SquWdjrLejN5emkFBWSzej1LdjR6S0uVdLC3SjCUBjV0RFO0dqr2ejkFSjyydWd0BFk4Bjx5BWdydWlzBjC3djx4d0DWSjDWdFB4dWhyd0dVdmgFBjRUSmr3dL14SjxFS0dVBWkHBqh1BL1USqr2B013B0V1BLCLBjtLeJR5BLhVd0rURjD1Smd0Sjr6RWhVdJd1'
new_c = []
for i in range(len(c)):
    if c[i] != '=':
        new_c.append(correct_table[table.index(c[i])])
    else:
        new_c.append(c[i])
n2 = int(base64.b64decode(''.join(new_c)).decode(), 16)
print("n2: ", n2)

c = 'BWhVdmg3Bj15RWR6dLVzRjdVRjBLeJO1dqBUBJr5eJg4B0BLSJrUSjC3BJNLRmr6d0g2Rj12B0uVSWRGequzdJgGdJIyBFBGSJBLdqyWB0r2B0gGej1GRmkLBWSzeqR2B0xUBLlVd0r6BLhWemlWd0dVemN3d0O0dqDzdWN4dFBUBjBLRFI1dqRGBWBURmrGS0k5dmgLS0u1BqRGR0R5equ1BLDVdqB2dWB2RmSVRFlySjCLBmBLBjrFRFdWejuyRFI1SJN6RmR2BWg2djV0d0I0SjD1S0uzdjS0SjIVBJOyBjl0S0NHRml1djg5djR5dmIyejBUeJSzdq12Sjlz'
new_c = []
for i in range(len(c)):
    if c[i] != '=':
        new_c.append(correct_table[table.index(c[i])])
    else:
        new_c.append(c[i])
c2 = int(base64.b64decode(''.join(new_c)).decode(), 16)
print("c2: ", c2)

c = 'BWh1BLDzBqxFS0I0eJSydLxFBJl1dmd1SjIVBqOyBqR6SjxGB0OySj1HB0B3dLVWdLR2Sql1RjxFSmB6djDzBWhWSmkFejB2dqRLRjCFR0rLBFgGejI0BFdWRWk3S0xHRjgLRWSySjuWB0l0SWNLSmSzd0I0BjDyRjt5BJIydLSVB0N6ejN2Bj1HdWSzBjSWBmIVBLhyeqRGRFNGRWrFdqI1djRLdFNGBJrUB0C6dLgGemkURLrHSqrLdLN4djVydJk4dJrGB01HRLlzB0tUSWrFSqx2RmO0BmN2d0SzB0VzRWrHRjIyBWlyemkHRmg3d0y0BjhyS0rGRLhWdjDV'
new_c = []
for i in range(len(c)):
    if c[i] != '=':
        new_c.append(correct_table[table.index(c[i])])
    else:
        new_c.append(c[i])
hint2 = int(base64.b64decode(''.join(new_c)).decode(), 16)
print("hint2: ", hint2)

c = 'BLkGdjr2BqO1Sjd0R0DWd0gHBjg3BmrGR0BFd0lzBFh1Sqr3RLVWBJI1BqtLejy0dJlVBLl0BqIWS016dWh1B0k2dmh0dqI1dj15SWdydjyzdqx3Sjd0Sqr5dJgGRLDyd0t5ejSWejlWRFlzRL1LejIWBjD0eqV1Smg6R0IVS0dVdjC5dJIzeJSVdmlyBLdVBWIWR0I0SqVyS0u1eqhWRFr5dFk3dWkGdjVzBjBFdjtHRLNUS0RGemrFdJR4SjN4d0C2ejOVSmk6d0yyS0NLBqhWdFBFeqVVRFkFBJrUdqIzRjx5BqD1SqD1BWIWBmr2djgUemIWSqr4RFRUSmIy'
new_c = []
for i in range(len(c)):
    if c[i] != '=':
        new_c.append(correct_table[table.index(c[i])])
    else:
        new_c.append(c[i])
hint3 = int(base64.b64decode(''.join(new_c)).decode(), 16)
print("hint3: ", hint3)

c = 'RLC6eJIWBLOVdj14ejyWBjx6BqkUSjCUSqg2d0d0BLhydLIzdmhzejy1BJg3BLxLBqk5BqO0SjRHRFhydLOWd0xUdLR4dWS1eJgUBLdzdjrFBLdVd0d0d0dzSjkURFBLdqk2Sjy1Bqh1B0xGSmhyBLkLdmR6BmrHRL12ejSWemk3R0R6Smh0eqIVR01GBmg3dmNUSmd0B0DzdJgFd0t5dLCUSjtLRmR5BjD1BmOVS012BjdVejtHd0CLBWg6d0yWSqu1B0gLSqC5RFdzSJOVR0CGdjuVdmr3RmSWRWBUdLSVeqdWeqlzSJkFeqkFBjy1dj16SWk6BFgGdjgUBjVyBx=='
new_c = []
for i in range(len(c)):
    if c[i] != '=':
        new_c.append(correct_table[table.index(c[i])])
    else:
        new_c.append(c[i])
a = int(base64.b64decode(''.join(new_c)).decode(), 16)
print("a: ", a)

from gmpy2 import gcd, invert

e1 = 2323
e2 = 2424
a1 = 2023
a2 = 2024
q2 = gcd(pow(a2, (-e2 * e1), n2) * pow(hint3, e1, n2) - pow(a1, (-e1 * e2), n2) * pow(hint2, e2, n2), n2)
# p2 = gcd(pow(a1, (-e1 * e2), n2) * pow(hint2, e2, n2) - pow(a2, (-e1 * e2), n2) * pow(hint3, e1, n2), n2)
p2 = n2 // q2
print("p2: ", p2)
print("q2: ", q2)

phi2 = (p2 - 1) * (q2 - 1)
d2 = invert(44021, phi2)
q = pow(c2, d2, n2)

p1 = gcd(n1, pow(2024, n1, n1)-hint1)
q1 = n1 // p1
print("p1: ", p1)
print("q1: ", q1)
phi1 = (p1-1)*(q1-1)
d1 = invert(39847, phi1)
p = pow(c1, d1, n1)
print("p: ", p)

na = int("9c5ab7c1cc9a4f60b1d53afafd7016d00e811e5a1c6fb258c75a246a0630a75644100828e21757de1d9a5ff99ebd05257aa9d895c1de40a2eb619fa52f32b38acb52669841d528351df863137b0a14f4aff6506cf0c7cdf1801c2bd3d7fb4e583811f4f771f7e5c0e5f42a85839affed38df8b913fa6a4e782adc028e5e86162f", 16)
ma = int("488d156b0cbef000f1bf6c47006a3595", 16)
print(ma)
print(na)

e = 3035716141
phi = (p-1)*(q-1)
d = invert(e, phi)
flag = pow(cc, d, p*q)
print(long_to_bytes(flag))