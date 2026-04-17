class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper = {}
        for num in nums:
            if num in mapper:
                mapper[num]+=1
            else:
                mapper[num]=1
        
        for val in mapper.values():
            if val > 1:
                return True
        
        return False