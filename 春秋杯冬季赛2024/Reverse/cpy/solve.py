xor_list = [0xf656460d, 0xda144260, 0xeef1c943, 0xe4390f66]
cmp_list = [0xfbbc7f84591ff393, 0x360c751ee6bd9abd, 0x60854fc80d82350a, 0x139692ebf3ee3c4f, 0x8571b17650a42bd4]
# input_list = []
# input_list1 = [int.from_bytes(input_list[i:i+8], 'little', ) for i in range(0, len(input_list), 8)]
# for data in input_list1:
#     for i in range(32):
#         idx = data & 3
#         data <<= 2
#         data &= 0xffffffffffffffff
#         data ^= xor_list[idx]

for data in cmp_list:
    for i in range(32):
        idx = data & 3
        if idx == 0:
            data ^= xor_list[1]
            data = (data >> 2) | (1 << 62)
        elif idx == 1:
            data ^= xor_list[0]
            data = (data >> 2) | (0 << 62)
        elif idx == 2:
            data ^= xor_list[3]
            data = (data >> 2) | (3 << 62)
        else:
            data ^= xor_list[2]
            data = (data >> 2) | (2 << 62)
    print(data.to_bytes(8, 'little').decode(), end="")