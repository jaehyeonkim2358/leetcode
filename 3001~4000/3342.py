class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        INF = float('inf')
        N, M = len(moveTime), len(moveTime[0])
        visited = [[INF for _ in range(M)] for _ in range(N)]
        move = ((0,1),(1,0),(0,-1),(-1,0))
        queue = [(0, 0, 0, 0)]
        while queue:
            cur = heappop(queue)
            if cur[2] == N - 1 and cur[3] == M - 1: return cur[0]
            for m in move:
                nr, nc = cur[2] + m[0], cur[3] + m[1]
                if not self.check(nr, nc, N, M): continue

                move_t = 1 if cur[1] % 2 == 0 else 2
                remain_t = max(0, moveTime[nr][nc] - cur[0])
                cost = cur[0] + remain_t + move_t
                if visited[nr][nc] <= cost: continue

                visited[nr][nc] = cost
                heappush(queue, (cost, cur[1] + 1, nr, nc))

    def check(self, r, c, n, m):
        if r < 0 or r >= n: return False
        if c < 0 or c >= m: return False
        return True
