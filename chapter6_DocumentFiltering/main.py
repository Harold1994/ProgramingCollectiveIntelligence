import chapter6_DocumentFiltering.docclass
from chapter6_DocumentFiltering import docclass, feedfilter

# cl= docclass.fisherclassifier(docclass.getwords)
# cl.setdb('test1.db')
# docclass.sampletrain(cl)
# cl2=docclass.naivebayes(docclass.getwords)
# cl2.setdb('test1.db')
# print(cl2.classify('quick money'))
cl=docclass.fisherclassifier(feedfilter.entryfeatures)
cl.setdb('python_feed.db')
feedfilter.read('python_search',cl)