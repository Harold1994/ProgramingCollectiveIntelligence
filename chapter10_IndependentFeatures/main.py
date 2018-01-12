from chapter10_IndependentFeatures import newsfeatures
from chapter6_DocumentFiltering import docclass
allw,artw,artt = newsfeatures.getarticlewords()
wordmatrix,wordvec = newsfeatures.makematrix(allw,artw)
print(wordvec[0:10])
print(artt[1])
print(wordmatrix[1][0:10])
def wordmatrixfeatures(x):
    return [wordvec[w] for w in range(len(x)) if x[w]>0]
classifier = docclass.naivebayes(wordmatrixfeatures)
