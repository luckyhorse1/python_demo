# python通过re模块操作正则表达式
import re

# 将正则表达式编译成Pattern对象
pattern = re.compile("hello.*!")

# 使用pattern匹配文本，获取匹配结果，无匹配返回None
match1 = pattern.match('hello, xiaoma! How are you?')

match2 = re.search(pattern, "hello, xiaoma! How are you?")

match3 = re.match(pattern, "hello, xiaoma! How are you?")
if match3:
    #使用Match获取分组信息
    print(match3.group())

# re.compile("正则表达式", flag)
# flag 表示匹配模式, 可以用 | 表示同时生效
# re.I (IGNORECASE)：忽略大小写, 括号内是完整写法
# re.M (MULTILINE)：多行模式, 改变 ^ 和 $ 的行为
# re.S (DOTALL)：点任意模式, 改变 . 的行为
# re.L (LOCALE)：使预定字符类\w\W\s\S\b\B取决于当前区域设定
# re.U (UNICODE)： 使预定字符类取决于字符编码
# re.X (VERBOSE)：详细模式, 该模式下正则表达式可以是多行, 忽略空白字符, 并可以加入注释,