from matplotlib import pyplot as plt
import random

x = range(2, 26, 2)

y = [random.uniform(15,26) for i in range(12)]

# 每隔2绘制刻度
x_ticks_1 = range(2,26,2)

# 每隔0.5绘制刻度
x_ticks_2 = [i/2 for i in range(4, 49)]

# 上面一种太密集,可以使用切片
x_ticks_3 = x_ticks_2[::3]

plt.xticks(x_ticks_3)

plt.plot(x,y)

plt.show()
