import os

white_List=["+","-","*","/","_","g","e","l","t","(",")",".",","]
flag=os.environ.get("GEEK_FLAG") if os.environ.get("GEEK_FLAG")!=None else "SYC{test}"
banner='''     _      ____                       __  __       _   _
  __| | ___/ ___|  ___  _ __ ___   ___|  \/  | __ _| |_| |__
 / _` |/ _ \___ \ / _ \| '_ ` _ \ / _ \ |\/| |/ _` | __| '_ \\
| (_| | (_) |__) | (_) | | | | | |  __/ |  | | (_| | |_| | | |
 \__,_|\___/____/ \___/|_| |_| |_|\___|_|  |_|\__,_|\__|_| |_|

'''
def waf(s):
    if not s.isascii():
        exit("Please input ascii")
    for word in s:
        if word not in white_List:
            exit("hacker!!!!")
print(banner)
print("please do this math problem")
#9872
while True:
    try:
        result = input("99*100^60= ")
        waf(result)

        if 99 * 100 ^ 60 == eval(result):
            print("Congradulation!!!!! Here is your reward: " + flag)
        else:
            print("not right")
    except:
        print("error")