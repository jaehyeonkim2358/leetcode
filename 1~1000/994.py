class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        fresh_count = 0
        rotten_oranges = []
        for i in range(N * M):
            r, c = i//M, i%M
            if grid[r][c] == 1:
                fresh_count += 1
            elif grid[r][c] == 2:
                rotten_oranges.append([r, c, 0])
        if fresh_count == 0: return 0

        MOVE = ((0,1),(1,0),(0,-1),(-1,0))
        queue = deque(rotten_oranges)
        while queue:
            x, y, t = queue.popleft()
            for dx, dy in MOVE:
                new_x, new_y = x + dx, y + dy
                if not(0 <= new_x < N and 0 <= new_y < M): continue
                if grid[new_x][new_y] != 1: continue

                fresh_count -= 1
                if fresh_count == 0: return t + 1

                grid[new_x][new_y] = 2
                queue.append([new_x, new_y, t + 1])

        return -1
