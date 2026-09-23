class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        memo1, memo2 = {}, {}
        nums1 = nums[0:len(nums)-1]
        nums2 = nums[1:len(nums)]

        def dfs(i, arr, memo):
            if i > len(arr)-1:
                return 0
            if i in memo:
                return memo[i]
            # print(i, arr, memo)
            alternate_house = arr[i] + dfs(i+2, arr, memo)
            skip = dfs(i+1, arr, memo)
            result = max(alternate_house, skip)
            memo[i] = result

            return result

        return max(dfs(0, nums1, memo1), dfs(0, nums2, memo2))


