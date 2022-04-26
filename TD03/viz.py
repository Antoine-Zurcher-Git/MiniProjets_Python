from graphviz import Digraph

g = Digraph('G', filename='graph.gv')

g.edge('a', 'b')
g.edge('a', 'c')

print(g.source)

g.render(filename='img')
g.view()