class Solution:
    def countSubstrings(self, s: str) -> int:
        index, Len = 0, 0
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True #All diagonal have 1 element so always palindrome

        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         print(dp[i][j], end = " ")
        #state of dp[i][j] for these 2 pntr i,j do i have palindrome ?
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if Len < (j-i+1):
                        index = i
                        Len = j - i + 1
        cnt = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] == True:
                    cnt+=1

        return cnt
#  for initial two last lines of dp my j-i<=2 will be useful and after the length increase over 2 after 3rd line of dp array from bottom my dp[i+1][j-1] will be useful 
