
# 通过位置
s1 = '{}, {}'.format('xiaoma', 18)
s2 = '{0}, {1}'.format('xiaoma', 18)
s3 = '{1}, {0}'.format('xiaoma', 18)

# 通过关键字
s4 = '{name}, {age}'.format(name='xiaoma', age=18)
print(s4)