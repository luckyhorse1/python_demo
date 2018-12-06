from matplotlib import pyplot as plt
from matplotlib import font_manager

# 用条形图描述三部电影14,15,16号的票房
a = ['战狼', '速度与激情', '大峡谷']
b_14 = [1000, 800, 5000]
b_15 = [3000, 500, 1000]
b_16 = [7000, 100, 500]

bar_width = 0.1

x_14 = range(len(a))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width for i in x_15]

# 设置字体
my_font = font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')
x_ticks = a
plt.xticks(x_15, a, fontproperties=my_font)

plt.bar(x_14, b_14, width=bar_width, label='14号')
plt.bar(x_15, b_15, width=bar_width, label='15号')
plt.bar(x_16, b_16, width=bar_width, label='16号')

plt.legend(prop=my_font)

plt.show()
