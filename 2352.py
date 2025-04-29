from collections import List

class Solution:
    def rotate(self, grid: List[List[int]]) -> List[List[int]]:
        reval = []
        n = len(grid)
        for j in range(n):
            row = []
            for i in range(n):
                row.append(grid[i][j])
            reval.append(row)
        return reval

    def equalPairs(self, grid: List[List[int]]) -> int:
        grid2 = self.rotate(grid)
        answer = 0
        for r1 in grid:
            for r2 in grid2:
                if r1 == r2: answer += 1

        return answer
