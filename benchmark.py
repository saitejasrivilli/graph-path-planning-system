import networkx as nx
import numpy as np
import time

def generate_graph(n):
    G = nx.Graph()
    for i in range(n*3):
        a=np.random.randint(0,n)
        b=np.random.randint(0,n)
        G.add_edge(a,b)
    return G

sizes=[1000,3000,5000]

for n in sizes:
    G=generate_graph(n)
    start=time.time()
    nx.single_source_dijkstra_path_length(G,0)
    print(n,time.time()-start)
