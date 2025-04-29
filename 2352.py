from collections import List

class Solution:
    def tupleGrid(self, grid: List[List[int]], reverse: bool) -> List[tuple]:
        reval = []
        n = len(grid)
        for j in range(n):
            row = []
            for i in range(n):
                if reverse:
                    row.append(grid[i][j])
                else:
                    row.append(grid[j][i])
            reval.append(tuple(row))
        return reval

    def equalPairs(self, grid: List[List[int]]) -> int:
        grid1 = self.tupleGrid(grid, True)
        grid2 = self.tupleGrid(grid, False)
        answer = 0
        for r1 in grid1:
            for r2 in grid2:
                if r1 == r2: answer += 1

        return answer
