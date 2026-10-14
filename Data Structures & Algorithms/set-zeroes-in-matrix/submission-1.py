class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix),len(matrix[0])
        row, column = [1]*R,[1]*C

        for r in range(0, R):
            for c in range(0, C):
                if matrix[r][c] == 0:
                    row[r] = 0
                    column[c] = 0
        for r in range(0, R):
            for c in range(0, C):
                if row[r] == 0 or column[c] == 0:
                    matrix[r][c] = 0
        