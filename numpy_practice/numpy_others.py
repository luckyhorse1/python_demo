import numpy as np

# 获取数组中最大值,最小值的位置, 0轴是纵轴
a1 = np.array([[1,2,3,4], [5,6,7,8]])
pos_max = np.argmax(a1, axis=0)
pos_min = np.argmin(a1, axis=1)

print(pos_min)