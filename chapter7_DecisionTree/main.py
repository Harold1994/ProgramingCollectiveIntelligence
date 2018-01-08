from chapter7_DecisionTree import treepredict, zillow, hotornot

# tree = treepredict.buildtree(treepredict.my_data)
# treepredict.drawtree(tree,jpeg='treepredice.jpg')
# print(treepredict.mdclassify(['google','None','yes',None],tree))
# housedata=zillow.getpricelist()
# # print(housedata)
# housetree = treepredict.buildtree(housedata)
# treepredict.drawtree(housetree,'housetree.jpg')
l1=hotornot.getrandomratings(500)
print(len(l1))