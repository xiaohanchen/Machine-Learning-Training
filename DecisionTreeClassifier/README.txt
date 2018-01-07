Decision Tree Classifier:

what question to ask and when

Gni Impurity: measure amount of uncertainty of partitioned data (low value mean low uncertainty)
Information Gain: quantify how much uncertainty a question could reduce

1. predefine the questions you want to ask
2. find the question with best information gain at the node
3. build tree by recursively run "partition" method, which return either node or leaf
4.the branch ends when find the leaf