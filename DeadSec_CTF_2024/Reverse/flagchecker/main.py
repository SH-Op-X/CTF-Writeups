# Source Generated with Decompyle++
# File: main.pyc (Python 3.10)
from types import CodeType

def emulate(opcodes):
    exec(opcodes, globals())


def main():
    global chk, t, FLAG, checker
    chk = 0
    t = [92, 138, 226, 248, 124, 187, 195, 106, 182, 233, 9, 79, 134, 101, 53, 240, 196, 183, 141, 83, 84, 118, 226, 6, 251, 74, 94, 37, 117, 90]
    
    try:
        FLAG = list(input('Flag : ').encode())
    finally:
        pass
    print()
    return None
    import checker
    if chk == 4919:
        checker.check()
        for i, c in enumerate([11, 248, 141, 150, 27, 187, 195, 106, 182, 233, 9, 79, 134, 101, 53, 240, 196, 183, 141, 83, 84, 118, 226, 6, 251, 74, 94, 37, 117, 90]):
            t[i] ^= c
        print(''.join(map(chr, t)))
        return None
    None('Wrong')
    return None


if __name__ == '__main__':
    main()
    return None
