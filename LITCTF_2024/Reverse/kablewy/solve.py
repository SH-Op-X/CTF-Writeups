import re
from base64 import b64decode
with open("./kablewy.js") as f:
    content = f.read()
results = re.findall(r"\= \"(.*?)\"\n", content)
for i in results:
    a = b64decode(i.encode()).decode()
    r = re.findall(r"atob\(\"(.*?)\"", a)
    if len(r):
        b = b64decode(r[0].encode()).decode()
        print(re.findall(r"postMessage\(\'(.*?)\'", b)[0], end="")