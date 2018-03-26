from sklearn import datasets
import numpy as np
from sklearn import tree
from sklearn.metrics import confusion_matrix

puredata=np.loadtxt('data.csv',delimiter=',')
X=puredata[:,:30]
Y=[]

for x in puredata:
    Y.append(x[30])

clf=tree.DecisionTreeClassifier()
clf.fit(X,Y)

pred=clf.predict(X)
cm=confusion_matrix(Y,pred)

#print cm

tp=cm[0][0]
fp=cm[0][1]
fn=cm[1][0]
tn=cm[1][1]

accuracy=round(float(tp+tn)/float(tp+tn+fp+fn),4)
tnr=round(float(tn)/float(tn+fp),4)
tpr=round(float(tp)/float(tp+fn),4)

print "The Accuracy is  ",accuracy
print "True Negative is ",tnr
print "True Positive is ",tpr



