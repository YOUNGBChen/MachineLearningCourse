from sklearn.datasets import load_iris
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import random
import time

def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.clock()
        fn(*args, **kwargs)
        print("%s cost %s second" % (fn.__name__, time.clock() - start))
    return _wrapper

def get_data():
    iris = load_iris()
    data = iris.data
    result = iris.target
    return data,result
@time_me
def Model():
    Multinomial = MultinomialNB()
    Multinomial = Multinomial.fit(data_train,result_train)
    pred = Multinomial.predict(data_test)

data,result = get_data()
data_train,data_test,result_train,result_test = train_test_split(data,result, test_size=0.3)

Multinomial = MultinomialNB()
Multinomial = Multinomial.fit(data_train,result_train)
pred = Multinomial.predict(data_test)


Model()
print(pred)
print(accuracy_score(result_test,pred))