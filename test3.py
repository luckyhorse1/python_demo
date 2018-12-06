import numpy as np
import random


a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

b = a.reshape(2, 2, 2)

print(b)

print(b.flatten())


print(a)
print(a.shape)
# print(type(a))

b = range(10)

c = np.array(b)

d = np.arange(10)
# print(d)
