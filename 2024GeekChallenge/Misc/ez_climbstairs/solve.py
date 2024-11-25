from pwn import *

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        # 初始化dp数组，用来保存每个台阶的方法数
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        # 从第3个台阶开始，根据递推公式计算方法数
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] +dp[i - 3]
        return dp[n]

sys.set_int_max_str_digits(100000000)
r = remote("nc1.ctfplus.cn", port=30927)
s = Solution()
for i in range(100):
    content = r.recvuntil("：")
    stairs = content.decode().split()[1]
    count = s.climbStairs(int(stairs))
    print(stairs)
    r.sendline(str(count))
    r.recvline()
print(r.recv())