import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = './test.csv'

df = pd.read_csv(file_path, error_bad_lines=False)

temp_list = df['category'].str.split(',').tolist()

category_list = list(set([i for j in temp_list for i in j]))

#构建为0数组
df_zeros = pd.DataFrame(np.zeros((df.shape[0], len(category_list))), columns=category_list)

#赋值为1
for i in range(df.shape[0]):
    df_zeros.loc[i, temp_list[i]] = 1

# 计算每隔分类的总和
category_count = df_zeros.sum(axis=0)

# 排序
category_count = category_count.sort_values()

# 画条形图

x = category_count.index
y = category_count.values

plt.bar(x, y)
plt.show()