import pandas as pd


file_path = './directory.csv'
df1 = pd.read_csv(file_path)

# 统计中国每个省的星巴克的数量
china_data = df1[df1['Country'] == 'CN']

province_count = china_data.groupby(by='State/Province').count()['Brand']

print(province_count)
