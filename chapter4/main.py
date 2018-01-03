from chapter4 import searchengine

clawer = searchengine.crawler('searchindex.db')
clawer.calculatepagerank()
# e = searchengine.searcher('searchindex.db')
# e.query("functional programming")
