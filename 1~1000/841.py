class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(r, rooms, visited):
            if r in visited: return

            visited.add(r)
            for nxt in rooms[r]:
                if nxt in visited: continue
                dfs(nxt, rooms, visited)

        visited = set()
        dfs(0, rooms, visited)
        return len(visited) == len(rooms)
