import jieba
import pandas
from collections import Counter

#trigram  p(w3|w1,w2) = count(w1,w2,w3)/count(w1,w2)


corpus = pandas.read_csv('F:\py_workspace\\nlp_session\\nlp_data\movie_comments.csv')


# 缺失值补充
# _nan = corpus['comment'].fillna(0)
# print(corpus.iloc[49355])
# print(corpus.describe())
# print(corpus.isnull().describe())

corpus['comment'] = corpus['comment'].fillna('',axis=0)

allComments = ''.join(corpus.iloc[:].comment)

tokens = jieba.cut(allComments)
counts = Counter(tokens)
print(counts.most_common()[:10])


def _2_gram_model():

    pass