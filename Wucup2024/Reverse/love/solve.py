# cmp = [0x027627626F09D86D, 0x0276276267BB1378, 0x027627626F09D85C, 0x027627626F3B1366, 0x02762762634EC49B, 0x027627626EA7621A, 0x0276276267BB134B, 0x02762762656C4E53, 0x027627626F6C4E48, 0x027627626662759E, 0x0276276267BB131B, 0x02762762634EC449, 0x027627626EA761C5, 0x027627626289D7DF, 0x0276276261313A47, 0x0276276267BB12D6, 0x027627625EE2753D, 0x02762762637FFF04, 0x027627625F44EB43, 0x027627625E4EC3CF]
# v7 = len(cmp)
# v9 = 103
# flag = "WuCup{"
# for i in range(len(cmp)):
#     v10 = -1
#     for j in range(32, 123):
#         # data = 0
#         data = v7 ^ j
#         data *= v7
#         data <<= (v10 - v9)&0xff
#         data ^= (v10 + 1) - v7 * (v9 + 1)
#         data += ((v10 + 2) - v7) ^ ((v9 + 2) + v7)
#         data -= ((v9 + 3) + v7) * ((v10 + 3) + v7)
#         v2 = v9 + 4
#         v9 += 5
#         v3 = v2
#         v4 = v10 + 4
#         v10 += 5
#         data = data // (v3 - v4)
#         data &= 0xffffffffffffffff
#         if data == cmp[i]:
#             flag += chr(j)
# flag += "}"
# print(flag)

addr = 0x559DD249155F
for i in range(0x559DD2491768, 0x559DD249176D):
    idc.patch_byte(i, ord(idc.get_bytes(i, 1))^0x43)