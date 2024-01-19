
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)   # For undirected graph

    def bfs(self, start):
        visited = [False]*(len(self.graph))
        levels  = [-1]*(len(self.graph))
        parent = [-1]*(len(self.graph))

        traversal = []

        q = deque()
        
        # Starting node
        q.append(start)
        visited[start] = True
        levels[start] = 0
        # Parent is still gonna be -1 for start node

        while q:
            curr_node = q.popleft()
            # This is the place where you edit your node
            traversal.append(curr_node)
            for neighbor in self.graph[curr_node]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True
                    levels[neighbor] = levels[curr_node] + 1
                    parent[neighbor] = curr_node

        return traversal, levels, parent
                    
    def shortest_path(self, start, end):
        _, levels, parent = self.bfs(start)
        path = []

        while end != -1:
            path.append(end)
            end = parent[end]

        return path[::-1]

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

start_node = 1
end_node = 4

traversal, levels, parent = g.bfs(start_node)

print(traversal)
print(levels)
print(parent)

print(g.shortest_path(start_node, end_node))