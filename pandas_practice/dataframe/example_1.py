import pandas as pd
import numpy as np
import string

df1 = pd.DataFrame(np.arange(12).reshape(3,4), index=list(string.ascii_lowercase[:3]), columns=list(string.ascii_uppercase[-4:]))
print(df1)
