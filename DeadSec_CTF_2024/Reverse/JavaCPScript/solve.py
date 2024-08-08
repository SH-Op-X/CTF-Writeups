task = []
for i in range(2304-32, 2304):
    t = []
    for j in range(32, 126):
        data = i
        data ^= j
        if i % 8 != 0:
            data ^= ((data >> 6) | (data << 2))
            data ^= ((data >> 5) | (data << 3))
            data ^= ((data >> 4) | (data << 4))
            data ^= ((data >> 7) | (data << 1))
        else:
            data ^= ((data >> 7) | (data << 1))
            data ^= ((data >> 6) | (data << 2))
            data ^= ((data >> 5) | (data << 3))
            data ^= ((data >> 4) | (data << 4))
        t.append(data)
    task.append(t)
# print(task)
s = [3910918, 3921698, 3921709, 3820578, 3921671, 3893657, 3911025, 3932159, 3820987, 3820987, 3895614, 3822653, 3919793, 3913160, 3822626, 3896081, 3911023, 3910936, 3813209, 3869603, 3813122, 3913158, 3921672, 3810527, 3871544, 3871506, 3893694, 3919755, 3893639, 3895583, 3893664, 3895813]
s = s[::-1]
flag = ""
for i in range(len(s)):
    flag += chr(task[i].index(s[i])+32)
print(flag)