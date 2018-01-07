# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import graphviz

iris = load_iris()

print iris.feature_names
print iris.target_names
print iris.data[0],iris.data[50],iris.data[100]
print iris.target[0],iris.target[50],iris.target[100]  #3种花，各从0，50，100 index开始

testIndex = [0, 50, 100]

trainingData = np.delete(iris.data, testIndex, axis=0)
trainingTarget = np.delete(iris.target, testIndex)

testData = iris.data[testIndex]
testTarget = iris.target[testIndex]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(trainingData,trainingTarget)

print "expected result: %s" % (testTarget)
print clf.predict(testData)

dot_data = tree.export_graphviz(clf, out_file=None,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     special_characters=True)
graph = graphviz.Source(dot_data)
graph