class Skip32:
    FTABLE = [164,216,10,132,249,73,247,245,180,34,22,121,154,178,176,250,232,46,78,139,207,77,203,47,83,150,218,31,79,57,69,41,11,224,3,161,24,242,97,105,19,184,123,196,234,251,62,84,151,133,108,187,243,100,155,26,125,175,230,246,248,23,107,163,58,183,124,16,194,148,130,28,239,181,27,235,209,146,48,185,86,186,219,134,64,66,192,225,91,89,129,96,103,12,217,145,54,214,193,168,52,7,102,106,70,1,149,87,110,153,156,119,152,253,179,195,177,255,220,33,226,236,215,229,222,72,75,30,67,238,159,111,74,61,206,68,40,211,8,213,223,200,104,25,138,204,49,32,142,199,144,171,201,117,221,202,94,93,50,165,113,137,98,45,160,14,44,136,81,131,85,101,39,126,4,65,53,76,29,116,210,197,254,60,205,252,128,172,231,63,92,166,174,5,36,157,21,82,35,241,42,122,114,127,0,141,15,227,13,240,189,115,118,112,56,162,237,212,143,99,140,135,17,233,9,120,18,191,147,80,37,198,51,55,158,208,244,167,188,173,95,109,170,20,88,38,182,228,190,169,59,2,6,90,43,71]

    @staticmethod
    def checkpass(password, key):
        target = [52, 0x8E, 0xE2, 0xAC, 108, 94, 80, 51, 11, 0xFB, 68, 0xA4, 0xE7, 6, 0x7C, 0xDF, 100, 62, 0x74, 70]
        password_array = target.copy()
        # password_array = Skip32.string_to_ascii_array(password)
        if len(password_array) != 20:
            return False

        for i in range(0, len(password_array), 4):
            block = (password_array[i] << 24) | (password_array[i + 1] << 16) | (password_array[i + 2] << 8) | password_array[i + 3]
            encrypted_block = Skip32.eee(block, key)
            password_array[i] = (encrypted_block >> 24) & 0xFF
            password_array[i + 1] = (encrypted_block >> 16) & 0xFF
            password_array[i + 2] = (encrypted_block >> 8) & 0xFF
            password_array[i + 3] = encrypted_block & 0xFF

        print("".join(map(chr, password_array)))
        for i in range(len(target)):
            if target[i] != password_array[i]:
                return False
        return True

    @staticmethod
    def eee(value, key):
        v = [(value >> 24) & 0xFF, (value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF]
        Skip32.skip32(key, v, False)
        return (v[0] << 24) | (v[1] << 16) | (v[2] << 8) | v[3]

    @staticmethod
    def g(key, round, value):
        v5 = value & 0xFF
        v0 = (value >> 8) ^ Skip32.FTABLE[key[(round * 4) % 8] ^ v5]
        v5_1 = v5 ^ Skip32.FTABLE[key[((round * 4) + 1) % 8] ^ v0]
        v0_1 = v0 ^ Skip32.FTABLE[key[((round * 4) + 2) % 8] ^ v5_1]
        return (v0_1 << 8) | (Skip32.FTABLE[key[((round * 4) + 3) % 8] ^ v0_1] ^ v5_1)

    @staticmethod
    def skip32(key, data, encrypt):
        if encrypt:
            round_start, round_step = 0, 1
        else:
            round_start, round_step = 23, -1

        v3 = (data[0] << 8) | data[1]
        v5 = (data[2] << 8) | data[3]

        for _ in range(12):
            v5 ^= Skip32.g(key, round_start, v3) ^ round_start
            round_start += round_step
            v3 ^= Skip32.g(key, round_start, v5) ^ round_start
            round_start += round_step

        data[0] = (v5 >> 8) & 0xFF
        data[1] = v5 & 0xFF
        data[2] = (v3 >> 8) & 0xFF
        data[3] = v3 & 0xFF

    @staticmethod
    def string_to_ascii_array(s):
        return [ord(c) for c in s]

# 示例
if __name__ == "__main__":
    key = b"7d77cfe8"  # 8字节密钥
    password = "testpassword12345678"  # 20字节密码

    skip32 = Skip32()
    result = skip32.checkpass(password, key)