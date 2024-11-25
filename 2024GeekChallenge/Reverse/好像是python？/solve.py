# def func1(s, R):
#     result = []
#     for i in s:
#         if "A" <= i <= "Z":
#             result.append(chr((ord(i) - ord("A") + R) % 26 + ord("A")))
#         elif "a" <= i <= "z":
#             result.append(chr((ord(i) - ord("a") + R) % 26 + ord("a")))
#         elif "0" <= i <= "9":
#             result.append(chr((ord(i) - ord("0") + R) % 10 + ord("0")))
#         else:
#             result.append(i)
#     return "".join(result)
#
#
# def func2(s2):
#     key = "SYC"
#     length = 18
#     cipher = []
#     for i in range(length):
#         cipher.append((ord(s2[i]) ^ i) + (~ord(key[i % 3]) + 1))
#     return cipher
#
#
# input0 = input()
# a = 13
# b = 14
# c = a ^ (a + b)
# d = b * 100
# e = a ^ b
# m = e + (d - c * 4) - 1
# r = m % 26
# cipher1 = func1(input0, r)
# cipher2 = func2(cipher1)
# print(cipher2)
# num = [-1, -36, 26, -5, 14, 41, 6, -9, 60, 29, -28, 17, 21, 7, 35, 38, 26, 48]
# for i in range(18):
#     if cipher2[i] != num[i]:
#         print("wrong!")
#     else:
#         print("Rrrright!")


def func1(s, R):
    result = []
    for i in s:
        if "A" <= chr(i) <= "Z":
            result.append(chr((i - ord("A") - R) % 26 + ord("A")))
        elif "a" <= chr(i) <= "z":
            result.append(chr((i - ord("a") - R) % 26 + ord("a")))
        elif "0" <= chr(i) <= "9":
            result.append(chr((i - ord("0") - R) % 10 + ord("0")))
        else:
            result.append(chr(i))
    return "".join(result)


def func2(s2):
    key = "SYC"
    length = 18
    cipher = []
    for i in range(length):
        cipher.append((s2[i] - (~ord(key[i % 3]) + 1)) ^ i)
    return cipher


# input0 = input()
a = 13
b = 14
c = a ^ (a + b)
d = b * 100
e = a ^ b
m = e + (d - c * 4) - 1
r = m % 26
num = [-1, -36, 26, -5, 14, 41, 6, -9, 60, 29, -28, 17, 21, 7, 35, 38, 26, 48]
cipher2 = func2(num)
cipher1 = func1(cipher2, r)
import hashlib

print(cipher1)
print("SYC{" + hashlib.md5(cipher1.encode()).hexdigest() + "}")
