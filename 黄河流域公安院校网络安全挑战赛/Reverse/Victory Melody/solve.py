vm = [0x20, 0x10, 0x5B,
      0x20, 0x11, 0x58,
      0x20, 0x12, 0x56,
      0x20, 0x13, 0x6E,
      0x20, 0x14, 0x11,
      0x20, 0x15, 0x4E,
      0x20, 0x16, 0x00,
      0x40,
      0x11, 0x21,
      0x10, 0x00,
      0x30,
      0x10, 0x01,
      0x30,
      0x10, 0x02,
      0x30,
      0x10, 0x03,
      0x30,
      0x10, 0x04,
      0x30,
      0x10, 0x05,
      0x30,
      0x10, 0x06,
      0x30,
      0x10, 0x07,
      0x30,
      0x50,
      0x10, 0x07]
for i in range(0, 21, 3):
    print(chr(vm[i+2]^0x21), end="")