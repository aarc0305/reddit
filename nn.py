import csv
import numpy as np
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
X_train = np.array(lx)
y_train = np.array(ly)

print X_train.shape
print y_train.shape