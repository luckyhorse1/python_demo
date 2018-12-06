import numpy as np

# 数组保存为npy文件
a1 = np.array([[1,2,3,4],[5,6,7,8]])
# np.save('/home/xiaoma/Desktop/a1',a1)

# 从npy文件中加载数组
# a2 = np.load('/home/xiaoma/Desktop/a1.npy')

# 数组保存为txt文件, 默认保存的是float
a3 = np.array([[1,2,3,4], [5,6,7,8]])
# np.savetxt('/home/xiaoma/Desktop/a3.txt', a3)

# 从txt文件中加载数组
a4 = np.loadtxt('/home/xiaoma/Desktop/np_test_1.txt', skiprows=1, dtype=np.int8, comments='#', usecols=(0,2))

(a5,a6) = np.loadtxt('/home/xiaoma/Desktop/np_test_1.txt', unpack=True, comments='#', usecols=(0,2))

a7 = np.loadtxt('/home/xiaoma/Desktop/np_test_2.txt', delimiter=',')

print(a7)