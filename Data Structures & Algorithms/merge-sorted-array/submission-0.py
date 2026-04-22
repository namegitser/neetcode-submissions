class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1 #overall last index
        i,j = m-1, n-1 # last of nums1 and nums2

        while j>=0: # jab tk i have something in nums2
            if i>=0 and nums1[i]>nums2[j]: # if nums1 ka last is greater than nums2 then nums1[last] mei wahi daal do
                nums1[last] = nums1[i]
                i-=1
            
            else:
                nums1[last] = nums2[j] # case where nums2 ka last is bigger then nums1[last] mei nums2 ka daal do
                j-=1

            last-=1
        
