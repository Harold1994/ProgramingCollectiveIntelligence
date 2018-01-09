from chapter8_PriceModels import numpredict
from chapter8_PriceModels.numpredict import wineprice

data = numpredict.wineset2()
# sdata = numpredict.rescale(data,[10,10,0,0.5])
print(numpredict.crossvalidate(numpredict.weightedknn,data))
print(numpredict.crossvalidate(numpredict.knnestimate,data))
