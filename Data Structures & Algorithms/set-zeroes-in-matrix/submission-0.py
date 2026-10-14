class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0]) # Separate column boundary

        def pad_marker(i, j):
            # Fill the row and column with a temporary marker instead of 0
            for c in range(cols):
                if matrix[i][c] != 0: # Don't overwrite other original zeros
                    matrix[i][c] = None #Make it None so chain reaction doesn't happen(if i make 0 then the algo might think ohh another zero make the row col zero similarilly all become 0)

            for r in range(rows):
                if matrix[r][j] != 0:
                    matrix[r][j] = None

        # Pass 1: Find original zeros and mark their paths
        for i in range(rows):
            for j in range(cols): #Start at 0, end at cols
                if matrix[i][j] == 0:
                    pad_marker(i, j)

        # Pass 2: Convert all temporary markers to actual zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
