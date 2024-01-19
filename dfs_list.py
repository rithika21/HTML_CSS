
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
        self.path = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)   # For undirected graph

    def dfs(self, start):
        self.visited.add(start)
        self.path.append(start)

        for neighbor in self.graph[start]:
            if neighbor not in self.visited:
                self.dfs(neighbor)

        return self.path

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

start_node = 0

print(g.dfs(start_node))

