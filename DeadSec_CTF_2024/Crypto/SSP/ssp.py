MAX_N = 100
RAND_MAX = 10 ** 200 # You can't even solve with knapsack method

from random import randrange

for n in range(1, MAX_N + 1):

    print(f"Stage {n}")

    arr = [ randrange(0, RAND_MAX) for _ in range(n) ]
    counts = randrange(0, n + 1)
    
    used = set()
    
    while True:

        idx = randrange(0, n)
        used.add(idx)

        if len(used) >= counts:
            break
    
    s = 0
    for idx in used:
        s += arr[idx]
    
    for a in arr:
        print(a, end=' ')
    print(s)

    answer = list(map(int, input().split()))

    user_sum = 0
    for i in answer:
        user_sum += arr[i]
    
    if user_sum != s:
        print("You are wrong!")
        exit(0)

    print(f"Stage {n} Clear")

print("Long time waiting... Here's your flag.")

with open('./flag', 'r') as f:
    print(f.read())