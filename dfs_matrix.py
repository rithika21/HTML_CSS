
class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adj_matrix = [[0 for _ in range(self.v)] for _ in range(self.v)]
        self.visited = [False]*(self.v)
        self.path = []

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def dfs(self, start):
        self.visited[start] = True
        self.path.append(start)

        for neighbor in range(self.v):
            if self.adj_matrix[start][neighbor] == 1 and not self.visited[neighbor]:
                self.dfs(neighbor)

        return self.path

g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

start_node = 0

print(g.dfs(start_node))

