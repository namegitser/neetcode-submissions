class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #brute
        n = len(matrix)
        rotated = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated[j][n-i-1] = matrix[i][j]

        for i in range(n): #for mimicing inplace
            for j in range(n):
                matrix[i][j] = rotated[i][j]
