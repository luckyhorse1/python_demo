import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.zeros((2,4)), index=list('AB'), columns=list('WXYZ '))

df2 = pd.DataFrame(np.ones((3,3)), index=list('ABC'))

df3 = df2.join(df1)

print(df3)