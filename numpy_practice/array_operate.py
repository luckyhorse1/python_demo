import numpy as np

# 数组的运算

# 数组和单个数字运算
a1 = np.array([[1,2,3,4], [5,6,7,8]])

a2 = a1 + 2

# /0 的结果： 0/0 = nan (not a number), 数字/0 = inf (infinite)

# 数组和数组运算

a3 = np.array([[1,2,3,4], [5,6,7,8]])

a4 = np.array([[1,2,3,4], [5,6,7,8]])

a5 = a3 + a4

# 维数不同或维度不同时, 使用广播原则

