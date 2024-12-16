import rand0m

# rand0m.rand0m 输入异或0x9e3779b9，再右移11位，再rsa加密
# check长度25以上
flag = "aa"
print(list(map(hex, rand0m.rand0m(flag))))
flag = "aa" * 4
print(list(map(hex, rand0m.rand0m(flag))))
flag = "a" * 28
print(list(map(hex, rand0m.rand0m(flag)))) #
flag = "abcdef" * 4 + "012"
print(list(map(hex, rand0m.rand0m(flag))))
# flag = input("Please input: ")
if(rand0m.check(flag)):
    print("Congrats! Flag is: flag{"+flag+"}")
else:
    print(i)
    print("Wrong! Try again!")
# ['0xae0f3021', '0xaa0']
# ['0xd553bbc', '0xaaaaaaaaaaab54d5554a']
# ['0xc0dcedd5', '0xaaaaaaaaaaaab54d5554a']
# ['0x24e520ad', '0xabcdefabcdf073f7f0cb']