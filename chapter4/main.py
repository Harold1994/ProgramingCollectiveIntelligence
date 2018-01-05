from chapter4 import searchengine
from chapter4 import nn

# clawer = searchengine.crawler('searchindex.db')
# clawer.calculatepagerank()
# e = searchengine.searcher('searchindex.db')
# e.query("functional programming")

mynet = nn.searchnet('nn.db')
# mynet.maketables()
mynet.generatehiddennode([101, 103], [201, 202, 203])
print(mynet.getresult([101, 103], [201, 202, 203]))
