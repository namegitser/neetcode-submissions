class Solution:
    def climbStairs(self, n: int) -> int:
        #first see what dp[i] represents (state) here, dp[i] means number of ways i can get to ith stair dp[0] = 1 (1way as i am starting), dp[1] = 1 (1way as to get to 1st step i need to go 1 step) now for overy other next we have to check for previous 2 as i can take wither 1 or 2 step so looking at my previous 2 staircase that in how many attempts i reach to that stair. i'll just add those two to get to this new one.  
        dp = [0]*(n+1)
        dp[0] = 1 
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        # print(dp)
        return dp[n] #we are bubbling up our final answer
