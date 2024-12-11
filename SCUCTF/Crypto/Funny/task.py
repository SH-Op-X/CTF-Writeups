import random
import libnum
from Crypto.Util.number import bytes_to_long, long_to_bytes
# Welcome to 2024SCUCTF Freshman Game
print("Welcome to 2024 SCUCTF!")
print("Crypto的flag形式一般为scuctf{...} or SCUCTF{...}")
print("这是你的第一个flag")
flag = b'************'
flag = bytes_to_long(flag)
print(flag**2)
print("感受到数字的美好了吗？")
print("接下来完成下面的挑战")
print("Good luck!")
print()
# funny
hint = b'************'
# bytes_to_long()
m = b'***********'
p = libnum.generate_prime(1024)
q = libnum.generate_prime(1024)
n = p * q
print("give you some funny numbers")
# funny 1
print(p+q - p*q + random.randint(-0x401, +0x401)) 
# funny 2
print(bytes_to_long(m)*bytes_to_long(hint))
# funny 3
print(bytes_to_long(m)*n*bytes_to_long(hint) - 0x401)
# funny 4
print(pow(bytes_to_long(hint), 65537, n))




