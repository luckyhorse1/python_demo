import numpy as np

a1 = np.arange(12).reshape(3,4).astype('float')

a1[1,2:] = np.nan

a2 = a1[a1==a1]

c = np.isnan(a1)

print(c)