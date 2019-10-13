import pandas as pd
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

corpus = pd.read_csv('sqlResult_1558435.csv',encoding='gb18030')

# print(corpus.columns)
# print(corpus.head(10))
# print(corpus.iloc[0:10].content)
# print(corpus.count())

FILE = ''.join(list(corpus.iloc[0:100].content))

max_length = 100000
sub_file = FILE[:max_length]

print(FILE[:100])

def cut(string):
    return list(jieba.cut(string))

TOKENS = cut(sub_file)
print(len(TOKENS))

words_count = Counter(TOKENS)
words_with_fre = [ f for w,f in words_count.most_common()]
print(words_count.most_common()[:10])

# plt.plot(np.log(words_with_fre))
# plt.show()

_2_grams = [
    TOKENS[i] + TOKENS[i+1] for i in range(len(TOKENS)-1)
]
_2_gram_word_counts = Counter(_2_grams)

def get1_gram_count(word):
    if word in words_count : return words_count[word]
    else:
        return words_count.most_common()[-1][-1]
def get2_gram_count(word):
    if word in _2_gram_word_counts : return _2_gram_word_counts[word]
    else:
        return _2_gram_word_counts.most_common()[-1][-1]

def _2_gram_model(sentence):
    tokens = cut(sentence)

    probability = 1
    for i in range(len(tokens)-1):
        word = tokens[i]
        next_word = tokens[i+1]

        pro = get2_gram_count(word+next_word) / get1_gram_count(next_word)

        probability *= pro

    return probability

print(_2_gram_model('自本周（6月12日）起'))