from functools import reduce
from hashlib import sha256

acc = 0xCDCB4322E6C376CC4C2D8C199E0D1818D8F861C788CFC181BE067F06380CF318EDD8CF98D98D9A800
flag = ""
while acc:
    acc >>= 7
    if acc & 1 == 0:
        acc >>= 1
    flag += chr((acc^85)&0x7f)
flag = flag[::-1][1:]
print(flag)
group_1 = [
        int.from_bytes(flag[1::3].encode(), 'big') % 998244353 == 156881262,
        sha256(flag[-16:].encode()).hexdigest().endswith('dcf56476457880bf5b39b295416f267b7a636324baeae1fd'),
        reduce((lambda x, y: x ^ y), map(ord, flag)) == 2]
if not all(group_1):
    print('Wrong')
    exit(1)
else:
    print('Correct')