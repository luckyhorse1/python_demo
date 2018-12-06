import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.array([[1,1], [1,2]]), columns=list('ab'))

df2 = pd.DataFrame(np.array([[1,0],[2,1]]), columns=list('ac'))

df3 = df1.merge(df2)


print(df1)
print(df2)

print(df3)