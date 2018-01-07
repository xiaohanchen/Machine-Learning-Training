# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5)

from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
# 两种不同的classifier， 解决同一个问题
clfDT = tree.DecisionTreeClassifier()
clfKN = KNeighborsClassifier() #K-Nearest Neighbor

clfDT = clfDT.fit(x_train, y_train)
testResultDT = clfDT.predict(x_test)

clfKN = clfKN.fit(x_train, y_train)
testResultKN = clfKN.predict(x_test)

from sklearn.metrics import accuracy_score
print "DecisionTreeClassifier accuracy: ", accuracy_score(y_test, testResultDT)   #compare the predicted result and the expected result
print "KNeighborsClassifier accuracy: ", accuracy_score(y_test, testResultKN)   #compare the predicted result and the expected result