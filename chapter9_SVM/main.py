from svm import *
from svmutil import svm_train, svm_predict

from chapter9_SVM import advancedclassify
numericalset = advancedclassify.loadnumerical()
print(numericalset)
scaledset,scaledf = advancedclassify.scaledata(numericalset)
answers = [r.match for r in scaledset]
inputs=[]
for row in scaledset:
    j=1
    for i in range(len(row.data)-1):
        inputs.append({j:row.data[i]})
        j+=1
print(inputs[0:10])
# prob = svm_problem([1,-1],[{1:-5,2:0,3:-10}, {1:-1, 2:18, 3:-1}])
# param = svm_parameter()
# param.kernel_type+=RBF
# m = svm_train(prob,param)
# yt=[-1]
# print (svm_predict(yt,[{1:1, 2:0, 3:1}],m))

