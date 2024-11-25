from Crypto.Util.number import *
from pwn import xor

key = b'...'
flag = b'...'
assert len(key)==4

enc = bytes_to_long(xor(flag,key))

f1 = 4585958212176920650644941909171976689111990
f2 = 3062959364761961602614252587049328627114908
e1 = enc^f1
e2 = e1^f2
print(e2)

"""
10706859949950921239354880312196039515724907
"""