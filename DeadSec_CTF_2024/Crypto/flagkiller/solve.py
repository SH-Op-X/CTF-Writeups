output = "0e98b103240e99c71e320dd330dd430de2629ce326a4a2b6b90cd201030926a090cfc5269f904f740cd1001c290cd10002900cd100ee59269a8269a026a4a2d05a269a82aa850d03a2b6b900883"
flag = ""
for i in range(0, len(output), 5):
    value = int(output[i:i+5], 16)
    temp = []
    while value > 0:
        temp.append(value%3)
        value //= 3
    add = 0
    for j in range(len(temp)):
        temp[j] += add
        add = 0
        if temp[j] == 3:
            temp[j] = 0
            add = 1
        elif temp[j] == 2:
            temp[j] = -1
            add = 1
    if add == 1:
        temp.append(1)
    temp = temp[::-1]
    for j in temp:
        value = value * 2 + j
    flag += hex(value)[2:].zfill(3)
print(bytes.fromhex(flag[:-3])+bytes.fromhex(flag[-2:]))