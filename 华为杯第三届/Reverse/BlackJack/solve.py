flag = ""
for i in "mhzj}oR":
    flag += chr(ord(i)^0x29)
flag += "Bl4c"+chr(ord("k")-32)+"_"+chr(ord("J")+32)+chr(ord("a")-32)+"c"+chr(ord("k")-32)
for i in "\tg%\t0\x03"+chr(56)+chr(56)+"\x0f":
    flag += chr(ord(i)^0x56)
print(flag+"}")