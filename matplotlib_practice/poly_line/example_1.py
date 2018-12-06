from matplotlib import pyplot as plt
import random

x = range(2, 26, 2)

y = [random.uniform(15,26) for i in range(12)]

# 设置图片大小
plt.figure(figsize=(20,8), dpi=80)

plt.plot(x,y)

#保存图片
plt.savefig('./demo.png')

plt.show()

