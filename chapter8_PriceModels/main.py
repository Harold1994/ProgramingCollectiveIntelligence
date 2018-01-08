from chapter8_PriceModels import numpredict
from chapter8_PriceModels.numpredict import wineprice

data = numpredict.wineset1()
print(numpredict.crossvalidate(numpredict.weightedknn,data))
print(numpredict.crossvalidate(numpredict.knnestimate,data))
