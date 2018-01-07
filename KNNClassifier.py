# cons
# computation intense
# cannot represent the realtionship between features

from scipy.spatial import distance

def distanceBetweenPoints(a,b):
    return distance.euclidean(a,b)

class KNNCLassifer():

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        predictions = []
        for x_test_row in x_test:
            label = self.closestTarget(x_test_row)
            predictions.append(label)
        return predictions

    def closestTarget(self, x_test_point):
        best_fit_distance = distanceBetweenPoints(x_test_point, x_train[0])
        best_fit_label = y_train[0]
        for i in range(1, len(x_train)):
            distanceToTrainData = distanceBetweenPoints(x_test_point, x_train[i])
            if distanceToTrainData < best_fit_distance:
                best_fit_distance = distanceToTrainData
                best_fit_label = y_train[i]
        return best_fit_label





from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5)

clf = KNNCLassifer()
clf.fit(x_train, y_train)
predictedResult = clf.predict(x_test)

from sklearn.metrics import accuracy_score
print "self making KNN accuracy: ", accuracy_score(y_test, predictedResult)   #compare the predicted result and the expected result