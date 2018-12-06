import numpy as np

# 查看数据元素类型
a1 = np.array([1,2,3,4])
e_type = a1.dtype

# 指定数据类型
a2 = np.array([1,0,1,2], dtype=np.bool)
a3 = np.array([1,0,0,2], dtype='?')

# 修改数组的数据类型, 但是不改变原来的数组类型
a4 = np.array([1,2,3,4])
a5 = a4.astype('i1')
a6 = a4.astype(np.int8)

# 修改浮点型的小数位数
a7 = np.array([1.234, 12.324234])
a8 = np.round(a7, 2)