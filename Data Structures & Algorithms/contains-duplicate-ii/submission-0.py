class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapper = {}
        for i in range(len(nums)):
            if nums[i] in mapper:
                if abs(mapper[nums[i]] - i) <=k:
                    return True

            mapper[nums[i]] = i
        return False 
