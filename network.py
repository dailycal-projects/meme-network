import csv
import networkx as nx

G=nx.DiGraph()

with open('data/edges.csv', 'r') as edges:
	reader = csv.DictReader(edges)
	for row in reader:
		G.add_edge(row['source'], row['target'], weight=row['weight'])

with open('data/nodes.csv', 'r') as nodes:
	reader = csv.DictReader(nodes)
	for row in reader:
		G.add_node(row['id'], label=row['name'])

clique = nx.make_max_clique_graph(G)
nx.write_gexf(clique, 'clique.gexf')

Gcc = sorted(nx.weakly_connected_component_subgraphs(G), key=len, reverse=True)
G0 = Gcc[0]

nx.write_gexf(G0, 'giant.gexf')

#A = nx.nx_agraph.to_agraph(G)
#A.layout()
#A.draw('file.svg')