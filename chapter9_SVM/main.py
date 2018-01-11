from svm import *
from svmutil import svm_train, svm_predict

from chapter9_SVM import advancedclassify
numericalset = advancedclassify.loadnumerical()

scaledset,scaledf = advancedclassify.scaledata(numericalset)
answers = [r.match for r in scaledset]
inputs=[]
for row in scaledset:
    tempdict ={}
    for i in range(len(row.data)):
        tempdict[i] = row.data[i]
    inputs.append(tempdict)
prob = svm_problem(answers, inputs)
param = svm_parameter()
param.kernel_type = RBF
m = svm_train(prob,param)

yt=[0]
print (svm_predict(yt,[{0: 0.28125, 1: 0.0,2: 0.0, 3: 0.71875, 4: 0.0,5: 1.0, 6: 0.4, 7: 0.04029577694380898}],m))

