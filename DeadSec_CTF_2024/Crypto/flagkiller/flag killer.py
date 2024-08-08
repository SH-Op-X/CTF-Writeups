#!/usr/bin/python3

from binascii import hexlify

flag = hexlify(b'DEAD{test}').decode()

index = 0
output = ''

def FLAG_KILLER(value):
    index = 0
    temp = []
    output = 0
    while value > 0:
        temp.append(2 - (value % 4) if value % 2 != 0 else 0)
        value = (value - temp[index])/2
        index += 1
    temp = temp[::-1]
    for index in range(len(temp)):
        output += temp[index] * 3 ** (len(temp) - index - 1)
    return output


while index < len(flag):
    output += '%05x' % int(FLAG_KILLER(int(flag[index:index+3],16)))
    index += 3

print(output)