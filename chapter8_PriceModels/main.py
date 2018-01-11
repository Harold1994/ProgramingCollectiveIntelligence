from chapter8_PriceModels import numpredict
from chapter8_PriceModels.numpredict import wineprice


data = numpredict.wineset2()
costf = numpredict.createcostfunction(numpredict.knnestimate, data)
print(optimization.annealingoptimize(numpredict.weightdomain, costf))
# print(numpredict.probguess(data,[99,20],40,80))
