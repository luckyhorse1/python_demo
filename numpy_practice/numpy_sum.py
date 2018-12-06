import numpy as np

# 全累加
a1 = np.array([[1,2,3,4],[5,6,7,8]])
sum = np.sum(a1)

# 往x轴压缩
a2 = np.array([[1,2,3,4],[5,6,7,8]])
sum2 = np.sum(a2, axis=0)

# 往y轴压缩
a3 = np.array([[1,2,3,4],[5,6,7,8]])
sum_3 = np.sum(a3, axis=1)

# 往某个平面压缩
a4 = np.arange(27).reshape(3,3,3)

# 往xy平面压缩
a5 = np.sum(a4, axis=0)

# 往xz平面压缩
a6 = np.sum(a4, axis=1)

# 往yz平面压缩
a7 = np.sum(a4, axis=2)

print(a4)
print(a7)