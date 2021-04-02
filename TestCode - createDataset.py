#import LSTM_Prediction as lp
import pandas as pd
import numpy

dataframe = pd.read_csv('Deaths1.csv', usecols=[2], engine='python')
dataframe = dataframe.values
print("Length ",len(dataframe))
#print(type(dataframe))

#print(dataframe.head(4))

def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		# a = dataset[i:(i+look_back), 0]
		a = dataset[i, 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)

trainSize = int(len(dataframe)*0.67)
testSize = len(dataframe)-trainSize
#print(trainSize)
#print(testSize)


train = dataframe[0:trainSize,:]
test = dataframe[trainSize:len(dataframe),:]
#print(train[2:5])
#print(test[2:5])




lookBack = 1
trainX, trainY = create_dataset(dataframe, lookBack)
testX, testY = create_dataset(dataframe, lookBack)

print(trainX[:5], trainY[:5], end=" ")
print("Length x and y: ", len(trainX), len(trainY))
trainX=pd.DataFrame(trainX)
trainY=pd.DataFrame(trainY)

trainDset = pd.concat([trainX, trainY], axis=1)
trainDset.to_csv("TrainDset.csv")

# trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
# testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
#
# print(trainX)
