class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0: zeros.append((i, j))

        move = ((0,1),(1,0),(0,-1),(-1,0))
        while zeros:
            x, y = zeros.pop()
            for dx, dy in move:
                tx, ty = dx, dy
                while True:
                    nx = x + tx
                    ny = y + ty
                    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                        matrix[nx][ny] = 0
                    else:
                        break
                    tx += dx
                    ty += dy
