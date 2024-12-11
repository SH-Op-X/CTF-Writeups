def sub_401D25():
    global dword_5D54FC
    global dword_511FE0
    for i in range(2 * dword_5D54F8 - 1):
        if (dword_511FE0[i] < 2 * dword_5D54FC and dword_511FE0[i + 1] < 2 * dword_5D54FC and (dword_511FE0[i] ^ dword_511FE0[i + 1]) == 1):
            return 0
    return 1


byte_4E1280 = [0]*200032
dword_511FE0 = [0]*68505
def sub_401DE0(a1):
    global dword_5D54F4
    global dword_5D54F8
    global dword_511FE0
    if a1 == 2 * dword_5D54F8:
        result = sub_401D25()
        if result:
            result = (dword_5D54F4 + 1) % 1000000007
            dword_5D54F4 = (dword_5D54F4 + 1) % 1000000007
    else:
        i = 0
        while True:
            result = 2 * dword_5D54F8
            if i >= result:
                break
            if byte_4E1280[i] != 1:
                byte_4E1280[i] = 1
                dword_511FE0[a1] = i
                sub_401DE0(a1 + 1)
                byte_4E1280[i] = 0
            i += 1
    return result

dword_5D54F4 = 0
def sub_401EEB():
    global dword_5D54F4
    dword_5D54F4 = 0
    sub_401DE0(0)
    print(dword_5D54F4)
    return dword_5D54F4

dword_5D54F8 = 1
dword_5D54FC = 1
sub_401EEB()    # 0
dword_5D54F8 = 2
dword_5D54FC = 1
sub_401EEB()    # 12
dword_5D54F8 = 2
dword_5D54FC = 2
sub_401EEB()    # 8
dword_5D54F8 = 3
dword_5D54FC = 1
sub_401EEB()    # 480
dword_5D54F8 = 3
dword_5D54FC = 2
sub_401EEB()    # 336
dword_5D54F8 = 3
dword_5D54FC = 3
sub_401EEB()    # 240
dword_5D54F8 = 4
dword_5D54FC = 1
sub_401EEB()    # 30240
dword_5D54F8 = 4
dword_5D54FC = 2
sub_401EEB()    # 23040
# dword_5D54F8 = 5
# dword_5D54FC = 1
# sub_401EEB()    # 2903040
# dword_5D54F8 = 5
# dword_5D54FC = 2
# sub_401EEB()    # 2338560
dword_5D54F8 = 5
dword_5D54FC = 3
sub_401EEB()    # 1895040