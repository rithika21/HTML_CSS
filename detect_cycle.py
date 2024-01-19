
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited, rec_stack):
        if node in rec_stack:
            return True

        if node not in visited:
            visited.add(node)
            rec_stack.add(node)

            for neighbor in self.graph[node]:
                if self.dfs(neighbor, visited, rec_stack):
                    return True

            rec_stack.remove(node)

        return False
    
    def detect_cycle(self):
        for node in list(self.graph): 
            if node not in self.visited:
                if self.dfs(node, set(), set()):
                    return True
        return False

g = Graph()

g.add_edge(0, 5)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(5, 1)

print(g.detect_cycle())