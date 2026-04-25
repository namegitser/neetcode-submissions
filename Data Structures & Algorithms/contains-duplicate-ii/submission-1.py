class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            if r-l > k: 
                window.remove(nums[l]) # always lets you maintain a window of k elements
                l+=1
            
            if nums[r] in window: #if i see the element already in the window, i'll return True
                return True
            
            window.add(nums[r])

        return False

        