from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

x = range(120)
y = [random.uniform(20, 35) for i in range(120)]

# x轴显示几点几分
x_ticks_1 = ['10点{}分'.format(i) for i in x if i < 60]
x_ticks_1 += ['11点{}分'.format(i - 60) for i in x if i >= 60]

# 设置字体
my_font = font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')

plt.xticks(x[::5], x_ticks_1[::5], rotation=90, fontproperties=my_font)

plt.plot(x, y)

plt.show()

