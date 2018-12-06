import numpy as np

# 生成数字(开始数字, 结束数字, 步长), 类似于切片
a1 = np.arange(10)
a2 = np.arange(2,10,2)

# 生成1到5之间平均分配的10个数字
a3 = np.linspace(1, 5, 10)

# 生成初始值为0的3行4列数组
a4 = np.zeros((3,4))

# 生成初始值为1的3行4列数组
a5 = np.ones((3,4))

# 生成对角矩阵
a6 = np.eye(3)

# 生成网格矩阵
a7 = np.arange(1,5)
a8 = np.arange(5,10)
a9, a10 = np.meshgrid(a7,a8)
print(a9)
print(a10)