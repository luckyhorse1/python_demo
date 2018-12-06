import numpy as np

#查看数组的形状
a1 = np.array([1,2,3,4])
shape_a1 = a1.shape

# 查看每一维的大小
b1 = np.arange(12).reshape(3, 4)
shape_0 = b1.shape[0]
shape_1 = b1.shape[1]

# 修改数组的形状
a2 = np.array([[1,2,3,4], [5,6,7,8]])
a3 = a2.reshape(4,2)
a4 = a2.reshape(2,2,2)

# 查看每一维的大小
size_a2_0 = a2.shape[0]
size_a2_1 = a2.shape[1]

# 变成一维
a5 = a2.flatten()

# 转置, 三种方法
a6 = np.array([[1,2,3,4],[5,6,7,8]])
a7 = a6.transpose()
a8 = a6.T
a9 = a6.swapaxes(0,1)
