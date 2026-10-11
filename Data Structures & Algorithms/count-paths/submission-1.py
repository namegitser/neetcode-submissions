class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #recursion
        memo = {}
        def rec(r,c):
            print((r,c))
            if (r,c) in memo:
                return memo[(r,c)]

            if r>=m or c >=n:
                return 0

            if r == m-1 and c == n-1:
                return 1

            right_path = rec(r, c + 1)
            down_path = rec(r + 1, c)

            memo[(r,c)] = right_path + down_path
            return memo[(r,c)]

        return rec(0,0)







