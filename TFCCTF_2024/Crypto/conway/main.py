# from secret import generate_next_key, flag
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# initial = 11131221131211131231121113112221121321132132211331222113112211
#
# initial = generate_next_key(initial)
# print(initial)

# initial = generate_next_key(initial)
initial = 132113213221133112132113311211131221121321131211132221123113112221131112311332111213211322211312113211
h = hashlib.sha256()
h.update(str(initial).encode())
key = h.digest()

cipher = AES.new(key, AES.MODE_ECB)
# print(cipher.encrypt(pad(flag.encode(),16)).hex())
print(cipher.decrypt(b"f143845f3c4d9ad024ac8f76592352127651ff4d8c35e48ca9337422a0d7f20ec0c2baf530695c150efff20bbc17ca4c"))
