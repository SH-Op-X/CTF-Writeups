import itertools
import random

# result = b'n\xf1\xc7\xf3J\x90H\xb5\x00\xd0\x1c\x92T\x99;"\xa7\n\x9cy\xaa\x9cS\xb61\n\xd4\xb8'
# result = b'0\xb3;\xbb\x91u\xc5\x95\x19p\xa3\x0e\xdd\x998\x8e\xdb<b\xa2\xb07S\xd4O\x81\n\xa8'
# result = b"\xa1\xbe'N\x92\x83\xcc\xb53\xd0\x1c+\xb8\xb0\x8e\x80>\x16>\xa2\xefIS\x9eL\xf6-N"
result = b"\x82Ku\x96\xbb\xc2e\xc20\x93\x97\xaa\xd3\xaaZ\x17\x1bW\x97\x0c\xb8\xb5\x041\xb2HK\xca"
l = len(result)
print(l)
b = [0]*l
for k in range(200000, 2000000):
    m = 0
    for i in range(k, k+6):
        random.seed(i)
        for j in range(l):
            b[j] ^= random.randint(0, 255)
    for i in range(l):
        if b[i] > 128:
            m+=1
    if m < 2:
        print(b, k)

# s = "TFCCTF{"
# a = []
# for i in range(7):
#     a.append(ord(s[i])^result[i])
# a.append(ord("}")^result[-1])
# print(a)
# for i in a:
#     for j in b:
#         if i == j:
#             b.remove(i)
# print(b, len(b))
#
# s = result[7:-1]
# print([i for i in s], len(s))

nums = range(10)
ascii_letter = list(range(48, 58)) + list(range(65, 90)) + list(range(97, 124)) + [ord("_")]

a = [248, 231, 100, 13, 81, 120, 120, 245, 198, 57, 243, 239, 253, 213, 199, 190, 54, 97, 68, 82]
b = [181, 0, 208, 28, 146, 84, 153, 59, 34, 167, 10, 156, 121, 170, 156, 83, 182, 49, 10, 212]
# a2 = [30, 183, 58, 214, 231, 13, 81, 120, 176, 132, 198, 57, 243, 239, 253, 199, 54, 97, 68, 82]
# b2 = [149, 25, 112, 163, 14, 221, 153, 56, 142, 219, 60, 98, 162, 176, 55, 83, 212, 79, 129, 10]
# a3 = [30, 58, 214, 231, 81, 120, 120, 176, 132, 57, 243, 239, 253, 213, 199, 190, 54, 97, 68, 82]
# b3 = [181, 51, 208, 28, 43, 184, 176, 142, 128, 62, 22, 62, 162, 239, 73, 83, 158, 76, 246, 45]
# a4 = [58, 248, 231, 100, 197, 81, 120, 120, 176, 245, 198, 57, 243, 51, 253, 199, 190, 97, 68, 82]
# b4 = [194, 48, 147, 151, 170, 211, 170, 90, 23, 27, 87, 151, 12, 184, 181, 4, 49, 178, 72, 75]
# flag = []
# for x in range(20):
#     def f(x):
#         for i in range(20):
#             for j in range(20):
#                 for k in range(20):
#                     for l in range(20):
#                         if b1[x]^a1[i] == b2[x]^a2[j] and b2[x]^a2[j] == b3[x]^a3[k] and b3[x]^a3[k] == b4[x]^a4[l]:
#                             flag.append(181^a1[i])
#                             print(chr(181^a1[i]))
#                             return
#     f(x)
# print(flag)
a1 = [248, 231, 245, 198, 243, 239, 253, 213, 199, 190]
a2 = [100, 13, 81, 120, 120, 57, 54, 97, 68, 82]
b1 = [181, 208, 146, 153, 167, 156, 170, 156, 182, 212]
b2 = [0, 28, 84, 59, 34, 10, 121, 83, 49, 10]
# for n in itertools.combinations(a1, len(a1)):
#     flag = ""
#     for i in range(len(a1)):
#         if n[i] ^ b1[i] in ascii_letter:
#             flag += chr(n[i] ^ b1[i])
#         else:
#             break
#     if len(flag) == len(a1):
#         print(flag)
# for n in itertools.permutations(a2, len(a2)):
#     flag = ""
#     for i in range(len(a2)):
#         if n[i] ^ b2[i] in ascii_letter:
#             flag += chr(n[i] ^ b2[i])
#         else:
#             break
#     if len(flag) == len(a2):
#         print(flag)