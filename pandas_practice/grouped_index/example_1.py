import pandas as pd

file_path = './test.csv'

df = pd.read_csv(file_path)

grouped = df.groupby(by=[df['country'], df['state']]).count()

print(grouped.index)