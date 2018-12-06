from matplotlib import pyplot as plt
import random

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]

width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]

a = [random.randint(47, 5000) for i in range(12)]

plt.bar(range(len(interval)), a, width=1)

_x = [i - 0.5 for i in range(len(interval)+1)]

# _x_ticks = [interval[i] for i in _x]

plt.xticks(_x, interval+[150])

plt.grid()

plt.show()
