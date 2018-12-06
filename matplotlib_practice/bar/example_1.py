from matplotlib import pyplot as plt
from matplotlib import font_manager

a = ['邪不压正', '末代皇帝', '七月与安生', '影']
x = range(len(a))
y = [5.35, 10.20, 7.34, 4.34]

# 设置字体
my_font = font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')

x_ticks = a
plt.xticks(x, x_ticks, fontproperties=my_font)

plt.bar(x,y, width=0.2)

plt.show()