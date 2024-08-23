import numpy as np

# 创建一个二维numpy数组
arr = np.array([[4, -2, 7],
                [-1, 3, 0],
                [5, -6, 2]])
arr = np.arange(48).reshape(2,3,4,2)

# 按行计算绝对值
abs_arr = np.abs(arr)

# 按行排序
sorted_indices = np.argsort(abs_arr, axis=1)
sorted_indices = np.array([[0,1,0],[0,1,0],[0,1,0],[0,1,0]]).reshape(1,3,4,1)
print(sorted_indices)
sorted_arr = np.take_along_axis(arr, sorted_indices, axis=0)

print("原始数组：")
print(arr)

print("按行绝对值排序后的数组：")
print(sorted_arr)