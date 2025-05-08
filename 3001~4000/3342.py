from heapq import heappop, heappush

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        INF = float('inf')
        N, M = len(moveTime), len(moveTime[0])
        MOVE = ((0,1),(1,0),(0,-1),(-1,0))
        queue = [(0, 0, 0, 0)]
        while queue:
            cur = heappop(queue)
            if cur[2] == N - 1 and cur[3] == M - 1:
                return cur[0]

            for dr, dc in MOVE:
                nr, nc = cur[2] + dr, cur[3] + dc
                if not (0 <= nr < N and 0 <= nc < M): continue
                if moveTime[nr][nc] == -1: continue

                move_t = 1 if cur[1] % 2 == 0 else 2
                remain_t = max(0, moveTime[nr][nc] - cur[0])
                cost = cur[0] + remain_t + move_t
                moveTime[nr][nc] = -1 # 방문체크
                heappush(queue, (cost, cur[1] % 2 + 1, nr, nc))
