class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums = [1,2,1]
        n = len(nums) # 3
        ans = [0]*2*len(nums) # [0,0,0,0,0,0]
        for i in range(n): # 0,1,2
            ans[i] = nums[i]
            ans[i+n] = nums[i]

        return ans
