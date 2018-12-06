from sklearn.feature_extraction import DictVectorizer

"""
    字典特征抽取：
    把字典中的一些类别数据（即字符串数据，比如'city':'上海'）转换为特征值('city=上海')，是上海就是1，不是上海就是0。
"""


def dictvec():

    # 默认处理后返回的是sparse矩阵，如果设置sparse=False，则返回的是numpy中使用的矩阵(即ndarray，二位数组)
    vector = DictVectorizer(sparse=False)

    data = [{'city': '北京', 'temperature': 10},
            {'city': '上海', 'temperature': 24},
            {'city': '深圳', 'temperature': 30}]

    # 参数要么是字典，要么是包含字典的迭代器。
    # 返回的是sparse格式的矩阵。
    # sparse矩阵是scipy工具的矩阵格式，这种矩阵格式比较节约内存，方便读取处理。
    res = vector.fit_transform(data)

    print(vector.get_feature_names())  # 该方法获取特征值（即列索引）
    print(vector.inverse_transform(res))  # 该方法是传入转换后的数据，返回原来的数据

    print(res)
    return


if __name__ == '__main__':
    dictvec()
