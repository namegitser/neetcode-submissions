class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_sum = len(nums) # Start with n
        
        # XOR both the index and the value at the same time
        for i, num in enumerate(nums):
            xor_sum ^= i ^ num
            
        return xor_sum
