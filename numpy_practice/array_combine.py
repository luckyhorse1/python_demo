import numpy as np

# 垂直合并
a1 = np.ones((2,2))
a2 = np.eye(2)
a3 = np.vstack((a1,a2))

# 水平合并
a4 = np.hstack((a1,a2))
