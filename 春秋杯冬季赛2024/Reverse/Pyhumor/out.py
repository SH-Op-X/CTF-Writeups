# Source Generated with Decompyle++
# File: out.pyc (Python 3.10)

__humor_enter__()

try:
    from hashlib import sha256
    from functools import reduce
    flag = input('Enter your flag: ')
    group_1 = [
        int.from_bytes(flag[1::3].encode(), 'big') % 998244353 == 156881262,
        sha256(flag[-16:].encode()).hexdigest().endswith('dcf56476457880bf5b39b295416f267b7a636324baeae1fd'),
        reduce((lambda x, y: x ^ y), map(ord, flag)) == 2]
    if not all(group_1):
        print('Wrong')
        exit(1)
    acc = 0
    for i in flag:
        i = ord(i) ^ 85
        acc |= i
        acc <<= 7 if i & 1 else 8
    if acc == 0xCDCB4322E6C376CC4C2D8C199E0D1818D8F861C788CFC181BE067F06380CF318EDD8CF98D98D9A800:
        print('Right')
finally:
    return None
    print('Wrong')
    exit(1)
    return None
    print('Stop reverse engineering me, enjoy your day :)')
    exit(1)
    return None

