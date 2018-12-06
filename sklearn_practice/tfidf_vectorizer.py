from sklearn.feature_extraction.text import TfidfVectorizer
import jieba


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

def tfidf_vec():

    tf_vec = TfidfVectorizer()

    c1, c2 = cutword()

    res = tf_vec.fit_transform([c1, c2])
    print(tf_vec.get_feature_names())
    print(res.toarray())
    return None

if __name__ == '__main__':
    tfidf_vec()