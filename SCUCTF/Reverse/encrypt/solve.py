out = [0x8B, 0xD0, 0x36, 0x85, 0xA5, 0x05, 0xB8, 0x6B, 0xC0, 0x23, 0xF9, 0xEA, 0x69, 0xEA, 0x56, 0x88, 0x03, 0xD6, 0x87, 0xC6, 0x1A, 0x00, 0x78, 0x9F, 0xC5, 0x1B, 0xE1, 0x7B, 0xD0, 0x9F, 0x40, 0xE9]
print(len(out))
key = []
with open("num.txt") as f:
    nums = f.read()
nums = nums.split(", ")
nums = list(map(int, nums[4:-1]))
k = 0
i = 0
while k <= 99999:
    if nums[2*i] > nums[2*i+1]:
        out[k%32] += 5
        k += 1
    elif nums[2*i] < nums[2*i+1]:
        out[k%32] -= 3
        k += 1
    i += 1

for i in range(len(out)):
    key.append(out[i]&0xff)
print(key)
print(bytes(key).hex())

from binascii import unhexlify
print(bytes([188,241,87,174,222,182,65,44,49,84,10,139,242,67,231,25,236,31,40,103,251,153,161,224,126,164,90,212,57,24,169,10]).hex())
private_key_bytes = unhexlify("8499ff0ebe06892c69ccc2838a2b9769e48f28af23b9a12046fcea0499b01912")
public_key_bytes = unhexlify("a12768bb262522d74c16f5f45f26a943ea710ea65e2fb6bd58d2e9e6974f9262")

from cryptography.hazmat.primitives.asymmetric import x25519

# 生成私钥对象
private_key = x25519.X25519PrivateKey.from_private_bytes(private_key_bytes)

# 生成公钥对象
public_key = x25519.X25519PublicKey.from_public_bytes(public_key_bytes)  # 去掉前缀 0x04
# 计算共享密钥
shared_secret = private_key.exchange(public_key)
print("Shared Secret:", shared_secret.hex())


