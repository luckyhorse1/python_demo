import numpy as np

gb_file_path = '../resource/GBvideos.csv'
us_file_path = '../resource/USvideos.csv'

a1 = np.loadtxt(gb_file_path, delimiter=',', usecols=(5,6,7,8), skiprows=1)
print(a1)