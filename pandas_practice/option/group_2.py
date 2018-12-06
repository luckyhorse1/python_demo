import pandas as pd

file_path = './directory.csv'
df1 = pd.read_csv(file_path)

group = df1.groupby(by=['Country', 'State/Province'])


print(group['Country'].count())

data = df1['Country'].groupby(by=[df1['Country'], df1['State/Province']]).count()