class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        max_vol = 0
        while l<r:
            curr_vol = abs((l-r)*min(heights[l], heights[r]))
            max_vol = max(max_vol, curr_vol)
            
            if heights[l]<heights[r]:
                l+=1
            
            else:
                r-=1

        return max_vol
        
