class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0
        max_sum = nums[0]

        for n in nums:
            curr_sum = max(curr_sum, 0)#if curr_sum becomes negative start fresh from next element
            curr_sum += n
            max_sum = max(curr_sum, max_sum)

        return max_sum