class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        visited = [False] * self.V
        self.dfs_util(start_vertex, visited)


g = Graph(10)
edges = [(7, 3), (3, 1), (1, 0), (0, 2), (2, 5), (5, 4), (4, 8), (8, 6), (6, 9), (1, 4), (2, 6), (3, 8), (9, 7), (4, 9),
         (5, 7), (5, 1), (5, 3), (8, 0), (9, 1), (3, 6), (9, 5)]

for u, v in edges:
    g.add_edge(u, v)

start_vertex = 7
print("DFS начиная с вершины", start_vertex)
g.dfs(start_vertex)
