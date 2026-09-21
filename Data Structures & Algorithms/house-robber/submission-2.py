class Solution:
    def rob(self, nums: List[int]) -> int:
        #Memo
        #memo[key] = ? for house at this position what is my maximum profit taht i can get
        memo = {}

        def rob(i):
            if i in memo:
                return memo[i]

            if i < 0:
                return 0

            curr_and_nxt = nums[i] + rob(i-2)
            skip = rob(i-1)
            result = max(curr_and_nxt, skip)
            memo[i] = result
            return result

        return rob(len(nums)-1)