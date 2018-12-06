from pymongo import MongoClient

import pandas as pd

a1 = pd.read_csv('./animal_name_count.csv')

a1 = a1.sort_values(by='count_animal_name', ascending=False)

print(a1)
