Implementation:
1. need a CLASSIFIER
2. FIT the historical data
3. PREDICT result by giving a new input



TensorFlow: DeepLearning working well with images (images)
DeepLearning: using classifier called Neural Networking having multipal layers (e.g. edge learn layers, texture learn, shape learn.....)
TFLearn: ML lib on top of TensorFlow, which is retraining data of INCEPTION (google image classifier)
TensorBoard: is a monitoring and inspection tool included with tensorflow
Transfer Learning(Retrain): which means we are starting with a model that has been already trained on another problem. We will then be retraining it on a similar problem



ReTraining:
network = modal
1.Feeding in a higher resolution image takes more processing time, but results in better classification accuracy
2.By using pre-trained network (i.e. Inception V3 model or a MobileNet (lightweight)), to define the classification layer
3.Bottelneck:the layer just before the final output layer => it contains the cached date of calculating the layers behind the bottleneck for each image, the result of these lower layers' calculation doesnt change (since the layers doesnt change)
4.Final Layer: the layer actually does the prediction => By default, this script runs 4,000 training steps. Each step chooses 10 images at random from the training set, finds their bottlenecks from the cache, and feeds them into the final layer to get predictions. Those predictions are then compared against the actual labels to update the final layer's weights through a backpropagation process
5.performance: If the training accuracy is high but the validation accuracy remains low, that means the network is overfitting, and the network is memorizing particular features in the training images that don't help it classify images more generally.
                (意思是：如果accuracy 比 validation accuracy 高的话， 说明训练出来的modal在死记硬背一些training set 的数值)
6.cross entropy: 两个随机变量的相似程度


