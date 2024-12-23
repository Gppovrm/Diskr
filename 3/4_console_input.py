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


n, m, s = map(int, input().split())
g = Graph(n)
for _ in range(m):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start_vertex = s
print("DFS начиная с вершины", start_vertex)
g.dfs(start_vertex)
