#####################################
# Decision Tree and Classifier
# machine learning to categorise Apple and Orange
#####################################

from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0]]    #weight; texture: 1 smooth 0;
labels = [0,0,1,1]   # 0 apple 1 orange
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[160,0]])
