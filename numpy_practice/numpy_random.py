import numpy as np
from numpy import random as nr

# 只显示两位小数
np.set_printoptions(precision=2)

# 生成一个2行2列的随机数数组, 均匀分布
a1 = nr.rand(2,2)

# 生成一个2行2列的随机数数组, 正态分布
a2 = nr.randn(2,2)

# 生成一个随机数为整数, 且指定范围的2行2列数组, 均匀分布
a3 = nr.randint(0,10,(2,2))

# 生成一个随机数为小数, 且指定范围的2行2列数组, 均匀分布
a4 = nr.uniform(0, 10, (2,2))

# 生成一个随机数为小数, 分布中心为1, 标准差为5的2行2列数组
a5 = nr.normal(1, 5, (2,2))

# 设置种子, 以后每次生成的随机数都一样
nr.seed(5)
a6 = nr.randint(2,6, (3,4))
print(a6)