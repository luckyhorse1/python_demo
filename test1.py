import matplotlib
from matplotlib import pyplot as plt
import random
from matplotlib import font_manager
#
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': '12'}

# matplotlib.rc("font", **font)

a = ["站狼2", "速度与激情", '大峡谷']

my_font = font_manager.FontProperties(fname="/usr/share/fonts/truetype/arphic/ukai.ttc")

plt.figure(figsize=(20, 8), dpi=80)

bar_width = 0.1

x_14 = range(len(a))

x_15 = [i+bar_width for i in x_14]

x_16 = [i+bar_width*2 for i in x_14]

plt.bar(x_14, random.randint(0, 200), width=0.1, label='9.14')
plt.bar(x_15, random.randint(0, 200), width=0.1, label='9.15')
plt.bar(x_16, random.randint(0, 200), width=0.1, label='9.16')

plt.xticks(x_15, a)

plt.legend()
# _x_ticks = range(120)

# plt.xticks(x[::5], _x_ticks[::5], fontproperties=my_font)
plt.xlabel("time")
plt.ylabel("temp")
plt.title("10~12 temp change table")
# # plt.savefig("./demo.png")
plt.show()
