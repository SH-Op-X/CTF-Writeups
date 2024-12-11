def dp_solve(dword_5D54F8, dword_5D54FC):
    """
    动态规划求解转换版本
    dword_5D54F8: 状态总数的一半
    dword_5D54FC: 条件约束参数
    """
    total_states = 2 * dword_5D54F8
    dp = [0] * (total_states + 1)  # dp[a1] 表示从状态 a1 开始的合法方案数
    dp[total_states] = 1          # 到达终点，只有一种方案

    # 判断是否合法的辅助函数（等价于 sub_401D25）
    def is_valid(i, j):
        return (
            i < 2 * dword_5D54FC and
            j < 2 * dword_5D54FC and
            (i ^ j) == 1
        )

    # 从倒数第一个状态向前计算
    for a1 in range(total_states - 1, -1, -1):
        for i in range(total_states):
            if dp[a1 + 1] > 0:  # 检查下一步是否有可行解
                # 判断是否可以选择状态 i
                valid = True
                for j in range(a1):  # 遍历之前选的状态
                    if not is_valid(i, dp[j]):
                        valid = False
                        break
                if valid:
                    dp[a1] += dp[a1 + 1]

    return dp[0]  # 返回从状态 0 开始的方案数


# 测试
print(dp_solve(1, 1))  # 对应 dword_5D54F8=1, dword_5D54FC=1
print(dp_solve(2, 1))  # 对应 dword_5D54F8=2, dword_5D54FC=1
print(dp_solve(3, 2))  # 对应 dword_5D54F8=3, dword_5D54FC=2
