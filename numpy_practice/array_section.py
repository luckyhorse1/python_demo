import numpy as np

a1 = np.array([[1,2,3,4],[5,6,7,8],[7,8,9,10]])
# 取第一行
a2 = a1[0]

# 取连续的多行
a3 = a1[1:]

# 取不连续的多行
a4 = a1[[0,2]]

# 行是第一个参数, 列是第二个参数, 用法相同

# 取第一列
a5 = a1[:, 0]

# 取3行4列的值
a6 = a1[2,3]

# 取多个不相邻的点, 1行1列 3行4列
a7,a8 = a1[[0,2], [0,3]]