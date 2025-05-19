class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections_map = dict()
        reversed_connections_map = dict()
        for f, t in connections:
            if f not in connections_map: connections_map[f] = []
            connections_map[f].append(t)

            if t not in reversed_connections_map: reversed_connections_map[t] = []
            reversed_connections_map[t].append(f)

        visited = [False for _ in range(n)]
        self.count = 0
        def dfs(node):
            visited[node] = True
            if node in connections_map:
                for nxt in connections_map[node]:
                    if visited[nxt]: continue
                    self.count += 1
                    dfs(nxt)
            if node in reversed_connections_map:
                for nxt in reversed_connections_map[node]:
                    if visited[nxt]: continue
                    dfs(nxt)

        dfs(0)
        return self.count
