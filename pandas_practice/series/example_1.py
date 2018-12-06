import pandas as pd

a = {'no1':1,'no2':2,'no3':3,'no4':4}

s3 = pd.Series(a)
s4 = pd.Series(a, index=list('abcd'))

print(s3)
print(s4)

s1 = pd.Series([1, 2, 3, 4], index=list('abcd'))

temp_dict = {'name': 'xiaoma', 'age': 18}

s2 = pd.Series(temp_dict)

