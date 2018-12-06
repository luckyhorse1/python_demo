import numpy as np

# 深拷贝和浅拷贝
# numpy是处理大数据的, 所以x和y指向同一块内存空间
x = np.array([1,2,3,4])

y = x

y[0] = 2

# 如果想独立开来, 可以使用copy函数
m = np.array([1,2,3,4])

n = m.copy()

n[0] = 2

# 对于切片, b的数据由a保管, 所以他们的数据变化一致
a = np.array([1,2,3,4])
b = a[:]
a[0] = 0

print(b)