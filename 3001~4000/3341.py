class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        INF = float('inf')
        N, M = len(moveTime), len(moveTime[0])
        visited = [[INF for _ in range(M)] for _ in range(N)]
        move = ((0,1), (1,0), (0,-1), (-1,0))
        queue = [(0,0,0)]
        while queue:
            cur = heappop(queue)
            if cur[1] == N-1 and cur[2] == M-1: return cur[0]
            for m in move:
                new_r, new_c = cur[1] + m[0], cur[2] + m[1]
                if not self.check(new_r, new_c, N, M): continue

                remain_t = max(0, moveTime[new_r][new_c] - cur[0])
                cost = cur[0] + remain_t + 1
                if visited[new_r][new_c] <= cost: continue

                visited[new_r][new_c] = cost
                heappush(queue, (cost, new_r, new_c))

        return visited[N-1][M-1]

    def check(self, r, c, n, m):
        if r < 0 or r >= n: return False
        if c < 0 or c >= m: return False
        return True
