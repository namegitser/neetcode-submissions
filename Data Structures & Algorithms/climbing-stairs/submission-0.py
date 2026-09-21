class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def num_steps(num):
            if num in memo:
                return memo[num]

            if num < 0:
                return 0

            if num == 0:
                return 1
            
            result = num_steps(num-1) + num_steps(num-2)
            memo[num] = result
            return result

        return num_steps(n)