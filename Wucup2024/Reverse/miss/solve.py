cmp = [0x000000F5, 0x00000200, 0x00000208, 0x000001EF, 0x00000235, 0x00000274, 0x0000023A, 0x00000276, 0x000002B7, 0x00000306, 0x000002B2, 0x00000313, 0x000002E2, 0x0000032F, 0x00000371, 0x00000440, 0x00000338, 0x000003E9, 0x000003E2, 0x000003B6, 0x00000407, 0x0000043E, 0x000003BA, 0x000003F4, 0x00000415, 0x00000473, 0x000004DA]
# bruteforce
for k in range(27):
    for i in range(1, 128):
        data = i
        for j in range(27):
            if (j & 1) != 0:
                data = k + j + 2 + (k ^ data)
            else:
                data = k + j + 1 + (k ^ data)
        # print(data)
        if data == cmp[k]:
            print(chr(i), end="")