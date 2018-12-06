import numpy as np

# 全部相加求平均
a1 = np.array([[1,2,3,4],[5,6,7,8]])
mean1 = np.mean(a1)

# 往x轴压缩的方向求平均
mean2 = np.mean(a1, axis=0)

# 往y轴压缩的方向求平均
mean3 = np.mean(a1, axis=1)

a = np.array([1,2,3,4,np.nan])

mean = np.mean(a)