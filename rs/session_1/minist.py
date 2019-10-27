from sklearn import datasets
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.metrics import accuracy_score
import pickle

def read_data(data_file):
    import gzip
    f = gzip.open(data_file, "rb")
    # train, val, test = pickle.load(f)

    # 改：使用了_Unpickler对象，并且对象的构造函数使用了“bytes”编码，这样就能正确读取pickle格式的文件了
    Myunpickle = pickle._Unpickler(file=f, fix_imports=True, encoding="bytes", errors="strict")
    train, val, test = Myunpickle.load()

    f.close()
    train_x = train[0]
    train_y = train[1]
    test_x = test[0]
    test_y = test[1]
    return train_x, train_y, test_x, test_y


data_file = "F:/py_workspace/nlp_session/nlp_data/mnist.pkl.gz"
train_x, train_y, test_x, test_y = read_data(data_file)


# digits = datasets.load_digits()
# data =  digits.data
# target = digits.target
# print(data.shape)
# print(digits.images[0])
# print(digits.target)
# # plt.gray()
# # plt.imshow(digits.images[0])
# # plt.show()
# train_x,test_x,train_y,test_y = train_test_split(data,target,test_size=25,random_state=33)

ss = preprocessing.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.fit_transform(test_x)

# lr
model = LogisticRegression()

# 贝叶斯
# from sklearn.naive_bayes import MultinomialNB
# model = MultinomialNB(alpha=0.01)

# knn
# from sklearn.neighbors import KNeighborsClassifier
# model = KNeighborsClassifier()

# 随机森林
# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=8)

# 决策树
# from sklearn import tree
# model = tree.DecisionTreeClassifier()

# gbdt
# from sklearn.ensemble import GradientBoostingClassifier
# model = GradientBoostingClassifier(n_estimators=200)

# svm
# from sklearn.svm import SVC
# model = SVC(kernel='rbf', probability=True)

model.fit(train_x,train_y)

predict_y = model.predict(test_ss_x)

print(test_y)
print(predict_y)

accuracy = accuracy_score(test_y,predict_y)

print(accuracy)
