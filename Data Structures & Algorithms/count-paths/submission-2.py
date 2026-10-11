class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp
        dp = [[1]*n for _ in range(m)]
        #1 bcoz dp[0][0] will be automatically filled and rest will be updated using it

        for i in range(1,m):
            for j in range(1,n):
                print((i,j))
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print(dp)


        return dp[m-1][n-1]