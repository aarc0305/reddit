import csv
import numpy as np
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
# training data
lx=[]
ly=[]
with open('train.csv') as file:
	lines = csv.reader(file)
	count = 0
	for line in lines:
		if count == 0:
			count = count+1
			continue
		lx.append(line[0])
		ly.append(int(line[1]))
		#print str(count)+' '+str(line[0])
                #if count != int(line[0]):
                #       print str(line[0])+str(count)
                #       break
		count = count +1
X_total = np.array(lx)
y_total = np.array(ly)
indices = np.random.permutation(X_total.shape[0])
X_total = X_total[indices]
y_total = y_total[indices]

X_train = X_total[1000:]
y_train = y_total[1000:]
X_test = X_total[0:1000]
y_test = y_total[0:1000]

print X_train.shape
print y_train.shape


token = Tokenizer(num_words = 3000)
token.fit_on_texts(X_train)

X_train = token.texts_to_sequences(X_train)
X_train = sequence.pad_sequences(X_train, maxlen=200)
X_test = token.texts_to_sequences(X_test)
X_test = sequence.pad_sequences(X_test, maxlen=200)
print token.document_count

print X_train.shape
print y_train.shape
# keras training		
model = Sequential()
model.add(Embedding(output_dim=32,input_dim=3000,input_length=200))
model.add(Dropout(0.8))
model.add(Flatten())
model.add(Dense(256,activation='sigmoid'))
model.add(Dropout(0.8))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X_train,y_train,batch_size=100,epochs=25)
scores = model.evaluate(X_test,y_test)
print scores
