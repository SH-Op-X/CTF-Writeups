import re

with open("tree") as f:
    content = f.read()
v1 = list(map(int, re.findall(r"a1, (.*?)LL", content)))
v2 = list(map(int, re.findall(r"v28 = (.*?);", content)))
print(len(v1)==len(v2))
print(v1)
print(v2)
tree = [[] for i in range(128)]
for i in range(len(v1)):
    tree[v1[i]].append(v2[i])
tree = [sorted(i) for i in tree]
print(tree)
for i in set(v1):
    queue = [i]
    flag = ""
    while len(queue):
        flag += chr(queue[0])
        for j in tree[queue[0]]:
            queue.append(j)
        queue = queue[1:]
    if len(queue) == 0:
        print(f"{i}, {flag.encode()}")