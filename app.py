import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random
import time

st.title("Interactive Robot Path Planning Simulator")

# Sidebar controls
size = st.sidebar.slider("Grid Size", 15, 40, 25)
density = st.sidebar.slider("Obstacle Density", 0.05, 0.40, 0.15)
speed = st.sidebar.slider("Robot Speed", 0.05, 1.0, 0.2)

start_button = st.sidebar.button("Start Simulation")

# Grid graph
G = nx.grid_2d_graph(size, size)

start = (0,0)
goal = (size-1, size-1)

pos = {(x,y):(y,-x) for x,y in G.nodes()}

# generate obstacles
for node in list(G.nodes()):
    if random.random() < density and node not in [start,goal]:
        G.remove_node(node)

robot = start

plot = st.empty()

def compute_path():

    try:
        return nx.astar_path(G, robot, goal)
    except:
        return []

if start_button:

    for i in range(200):

        fig, ax = plt.subplots()

        # add moving obstacle
        if random.random() < 0.25:

            node = (random.randint(0,size-1),random.randint(0,size-1))

            if node not in [robot,goal] and node in G:
                G.remove_node(node)

        path = compute_path()

        if path and len(path)>1:
            robot = path[1]

        nx.draw(G,pos,node_size=10,alpha=0.3,ax=ax)

        nx.draw_networkx_nodes(G,pos,nodelist=[robot],node_color="red",node_size=200,ax=ax)
        nx.draw_networkx_nodes(G,pos,nodelist=[goal],node_color="green",node_size=200,ax=ax)

        if path:
            edges=list(zip(path,path[1:]))
            nx.draw_networkx_edges(G,pos,edgelist=edges,width=3,ax=ax)

        ax.set_title("Dynamic Path Replanning")

        plot.pyplot(fig)

        time.sleep(speed)
