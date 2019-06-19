#encoding=utf-8
import graphviz as gv

# png, pdf, svg
#g1 = gv.Graph(format='svg')  #沒箭頭
g1 = gv.Digraph(format='svg') #有箭頭
g1.node('A')
g1.node('A')

g1.node('B')
g1.node('C')

g1.edge('A', 'A')
g1.edge('A','B',"test")
# g1.edge('A', 'B')
# g1.edge("B", 'C')
# g1.edge('C', 'C')
print  g1.source

g1.render('graph\\demo65')
