# 1.去空格及特殊符号
# s = 'xiaoma '
# 去掉字符串左右两边的空格或字符, s2等价于s3
# s1 = s.strip()
# s2 = s.strip('xia')
# s3 = s.strip('aix')
# 去掉左边或者右边的空格或字符
# s4 = s.lstrip()
# s5 = s.rstrip()

# 2.字符串的拼接
# a = 'hello'
# a += ', xiaoma'

# 3.查找字符
# b = 'xiaoma'
# b1 = 'x'
# b2 = b.grouped_index(b1)

# 4.比较两字符串, 需要导入operator模块
# lt le eq ne ge gt : 小于 小于等于 等于 不等于 大于等于 大于

# import operator
# s = 'xiao'
# s1 = 'xiao'
# res = operator.lt(s, s1)

# 5.字符串中的大小写转换
# upper lower title capitalize swapcase：变大 变小 每个单词首字母大写 首字母大写 大写变小写，小写变大写

# s = 'Xiao mA'
# s1 = s.title()
# s2 = s.capitalize()
# s3 = s.swapcase()

# 6.字符串反转
# s = 'xiaoma'
# s1 = s[::-1]

# 7.查找字符串
# s = 'xiaoma'
# s1 = 'ma'
# res = s.find(s1)

# 8.分割字符串
# 法一
# s = 'xi,ao,ma'
# s1 = ','
# s2 = s[s.find(s1) + 1:]
# 法二
# s = 'xi,ao,ma'
# s1 = s.split(',')

# 9.计算字符串中出现频次最多的字母
# 法一
# import re
# from collections import Counter
# s = 'Hello, XiaoMa'
# s = s.lower()
# res = re.findall('[a-zA-Z]', s)
# count = Counter(res)
# count_list = list(count.values())
# max_value = max(count_list)
# max_list = []
# for k, v in count.items():
#     if v == max_value:
#         max_list.append(k)
# max_list = sorted(max_list)
# max_list[0]
# 法二
# from collections import Counter
# s = 'Hello, XiaoMa'
# count = Counter([x for x in s.lower() if x.isalpha()])
# m = max(count.values())
# max_list = sorted([x for (x, y) in count.items() if y == m])
# max_list[0]
# 法三
# import string
# s = 'Hello, XiaoMa'
# s = s.lower()
# print(s.count)
# max(string.ascii_lowercase, key=s.count)
