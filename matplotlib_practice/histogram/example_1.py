from matplotlib import pyplot as plt

a = [100,123,145,167,145,134,123,107,104,115,157]

bin_width = 3
d = (max(a) - min(a)) // bin_width

x_ticks = range(min(a), max(a)+d, d)
plt.xticks(x_ticks)
plt.hist(a,d, density=True)

plt.show()