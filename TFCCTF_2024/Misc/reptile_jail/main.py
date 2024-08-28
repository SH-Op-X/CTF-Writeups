import sys

print("This is a secure calculator")

inp = input("Formula: ")

sys.stdin.close()

blacklist = "()=@{}\\?/,!@#$%^&*1234567890:;<>|`~+'\""

for x in blacklist:
    if x in inp:
        print("Nice try")
        print("You are not allowed to use the following characters:")
        print(x)
        exit()

if any(x in inp for x in blacklist):
    print("Nice try")
    exit()

fns = {
    "__builtins__": {"help": help},
}

eval(inp, fns, fns)