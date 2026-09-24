class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(s): #Reached end
                # print('c1')
                return 1

            if s[i] == '0':
                # print('c2')
                return 0

            res = dfs(i+1) #All 1 digit done
            
            # print('for 2digit')
            if i+1 < len(s):
                if 10<= int(s[i]+s[i+1]) <= 26:
                    res+=dfs(i+2)

            memo[i] = res
            return res



        return dfs(0)

