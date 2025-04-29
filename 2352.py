from collections import List, Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = Counter(tuple(row) for row in grid)

        n = len(grid)
        answer = 0
        for j in range(n):
            row = []
            for i in range(n):
                row.append(grid[i][j])
            answer += cnt[tuple(row)]

        return answer
