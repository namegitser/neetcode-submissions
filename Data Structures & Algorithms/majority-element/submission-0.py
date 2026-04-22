class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mapper = {}
        for i in range(n):
            if nums[i] in mapper:
                mapper[nums[i]]+=1
            
            else:
                mapper[nums[i]]=1
        
        for key, value in mapper.items():
            if value > n/2:
                return key