from chapter4 import searchengine

e = searchengine.searcher('searchindex.db')
print(e.getmatchrows('functional programming'))
