class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        MOVE = ((0,1),(1,0),(0,-1),(-1,0))
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        while queue:
            cell = queue.popleft()
            for dx, dy in MOVE:
                new_x, new_y = cell[0] + dx, cell[1] + dy
                if not (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0])):
                    # The entrance does not count as an exit
                    if cell[0] == entrance[0] and cell[1] == entrance[1]:
                        continue
                    else:
                        return cell[2]
                if maze[new_x][new_y] == '+': continue
                if visited[new_x][new_y]: continue

                visited[new_x][new_y] = True
                queue.append((new_x, new_y, cell[2] + 1))

        return -1
