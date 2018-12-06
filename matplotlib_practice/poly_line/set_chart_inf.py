from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

x = range(120)
y = [random.uniform(20,35) for i in x]

# 设置字体
my_font = font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')

# 添加坐标说明
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度/单位(摄氏度)', fontproperties=my_font)

# 添加标题
plt.title('10点到12点温度变化', fontproperties=my_font)

# 绘制网格
plt.grid(alpha=1)

# 添加图例
plt.plot(x,y,label='自己')
plt.legend(loc='upper left', prop=my_font)

plt.show()
