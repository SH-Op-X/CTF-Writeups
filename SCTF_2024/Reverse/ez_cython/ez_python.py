# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.19 | packaged by conda-forge | (default, Mar 20 2024, 12:38:07) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: ez_cython.py
import cy

def str_hex(input_str):
    return [ord(char) for char in input_str]


def main():
    print("欢迎来到猜谜游戏！")
    print("逐个输入字符进行猜测，直到 'end' 结束。")
    while True:
        while True:
            guess_chars = []
            while True:
                while True:
                    char = input("请输入一个字符（输入 'end' 结束）：")
                    if char == "end":
                        break
                    elif len(char) == 1:
                        guess_chars.append(char)

                print("请输入一个单独的字符。")

            guess_hex = str_hex("".join(guess_chars))
            if cy.sub14514(guess_hex):
                print("真的好厉害！flag非你莫属")
                break

        print("不好意思，错了哦。")
        retry = input("是否重新输入？(y/n)：")
        if retry.lower() != "y":
            break

    print("游戏结束")


if __name__ == "__main__":
    main()

# okay decompiling .\ez_cython.pyc
