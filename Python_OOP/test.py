import networkx as nx
import matplotlib.pyplot as plt

colors = ['red', 'green', 'blue', 'yellow']
DG = nx.DiGraph()
DG.add_nodes_from(['ML', 'AI', 'BigData', 'Data'])
DG.add_edges_from([('ML', 'AI'), ('ML', 'BigData'), ('ML', 'Data'), ('Data','ML')])
nx.draw(DG,with_labels=True, node_size=900, node_color = colors,alpha =0.3)
plt.show()

