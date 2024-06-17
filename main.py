import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

# Funkcja do obliczania sił działających na wierzchołki
def calculate_forces(graph, pos, k, t):
    displacement = {v: np.zeros(2) for v in graph.nodes}
    for u, v in graph.edges:
        delta = pos[u] - pos[v]
        distance = np.linalg.norm(delta)
        if distance > 0:
            force = (distance - k) * delta / distance
            displacement[u] -= force
            displacement[v] += force

    for u in graph.nodes:
        for v in graph.nodes:
            if u != v:
                delta = pos[u] - pos[v]
                distance = np.linalg.norm(delta)
                if distance > 0:
                    force = k**2 / distance * delta / distance
                    displacement[u] += force

    for v in graph.nodes:
        pos[v] += t * displacement[v]

# Funkcja do aktualizacji pozycji wierzchołków
def update_positions(num, graph, pos, k, t):
    calculate_forces(graph, pos, k, t)
    ax.clear()
    nx.draw(graph, pos, ax=ax, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold", font_color="white")

# Generowanie przykładowego grafu
nodes = ['Petyr','Varys','Tyrion','Cersei','Jofrey','Ned','Jorah','Viserys','Denerys','Robert','Margery','Olenna','Robb','Stannis','Theon']
edges = [   ('Petyr','Varys'),
            ('Petyr','Tyrion'),
            ('Tyrion','Cersei'),
            ('Petyr','Jofrey'),
            ('Ned','Jofrey'),
            ('Ned','Petyr'),
            ('Jorah','Varys'),
            ('Viserys','Varys'),
            ('Jorah','Denerys'),
            ('Viserys','Denerys'),
            ('Robert','Cersei'),
            ('Robert','Varys'),
            ('Margery','Cersei'),
            ('Olenna','Jofrey'),
            ('Robb','Jofrey'),
            ('Stannis','Jofrey'),
            ('Robb','Theon')
         ]

graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_edges_from(edges)

# Inicjalizacja pozycji wierzchołków
pos = {node: np.random.rand(2) for node in graph.nodes}

# Parametry algorytmu
k = 0.3  # Stała sprężystości
t = 0.3  # Współczynnik tłumienia

fig, ax = plt.subplots(figsize=(14, 10))

# Tworzenie animacji
ani = FuncAnimation(fig, update_positions,frames=1000, fargs=(graph, pos, k, t), interval=100)

plt.show()
