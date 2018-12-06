from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

x = range(120)
y = [random.uniform(20, 35) for i in range(120)]

# 设置线的样式
plt.plot(x,y, color='#DB7093', linestyle='--', linewidth=1, alpha=0.5)

plt.show()