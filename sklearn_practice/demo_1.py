from sklearn.feature_extraction.text import CountVectorizer

vector = CountVectorizer()

# 转换数据
res = vector.fit_transform(['life is short, i like python', 'life is too long, i dislike python'])

print(vector.get_feature_names())

print(res.toarray())