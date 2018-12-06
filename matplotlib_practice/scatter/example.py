from matplotlib import pyplot as plt
import random

x = range(31)
y = [random.uniform(10,30) for i in x]

plt.scatter(x,y)

plt.show()