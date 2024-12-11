c = [32, 42, 11, 34, 4, 45, 34, 42, 46, 42, 26, 42, 30, 7, 7, 48, 3, 4, 5, 3, 12, 11, 5, 32, 5, 12, 5, 7, 9, 30, 12, 10, 10, 32, 4, 12, 8, 18, 32, 48, 30, 5, 46, 10, 11, 11, 2, 33, 27, 42]
key_dict = {0x1E: "A", 0x30: "B", 0x2E: "C", 0x20: "D", 0x12: "E", 0x21: "F", 0x22: "G", 0x23: "H", 0x17: "I", 0x24: "J", 0x25: "K", 0x26: "L", 0x32: "M", 0x31: "N", 0x18: "O", 0x19: "P", 0x10: "Q", 0x13: "R", 0x1F: "S", 0x14: "T", 0x16: "U", 0x2F: "V", 0x11: "W", 0x2D: "X", 0x15: "Y", 0x2C: "Z", 0x02: "1", 0x03: "2", 0x04: "3", 0x05: "4", 0x06: "5", 0x07: "6", 0x08: "7", 0x09: "8", 0x0A: "9", 0x0B: "0", 0x2a: "[shift]", 0xc: "-", 0x1a: "{", 0x1b: "}"}
flag = ""
for i in range(len(c)):
    if c[i] not in key_dict.keys():
        print(c[i])
        continue
    if c[i] == 42:
        continue
    elif c[i+1] == 42:
        flag += key_dict[c[i]]
    else:
        flag += key_dict[c[i]].lower()
print(flag)