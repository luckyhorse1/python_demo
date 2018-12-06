from sklearn.feature_extraction.text import CountVectorizer
import jieba


def textvec():
    vector = CountVectorizer()
    data = ['life is short , i like python', 'life is too long, i dislike python']

    # 此函数的作用：
    # 1.先统计所有文章的词，重复的算作一个，得到词的列表
    # 2.对每篇文章， 在词的列表里面进行统计每个词出现的次数
    # 3.单个字母，我们不统计（因为，单个字母一般不能反映文章的主题信息，没有什么价值）
    res = vector.fit_transform(data)

    print(vector.get_feature_names())
    print(res.toarray())

    return None


def cutword():
    data1 = '人生苦短，我喜欢可乐。'
    data2 = '人生太长了，我不喜欢可乐。'

    con1 = jieba.cut(data1)
    con2 = jieba.cut(data2)

    # 转换为列表
    content1 = list(con1)
    content2 = list(con2)

    # 把列表转换为字符串
    c1 = " ".join(content1)
    c2 = " ".join(content2)

    return c1, c2


# 汉字的文本特征抽取，需要先进行分词
def chinese_vec():
    c1, c2 = cutword()
    print(c1, c2)

    vector = CountVectorizer()
    data = vector.fit_transform([c1, c2])
    print(vector.get_feature_names())
    print(data.toarray())


if __name__ == '__main__':
    chinese_vec()
