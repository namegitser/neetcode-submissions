class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True

        max_reachable_index = nums[0]

        for i in range(1,l):

            max_reachable_index -= 1

            if max_reachable_index < 0:
                return False

            max_reachable_index = max(nums[i], max_reachable_index)

            if i + max_reachable_index >= l - 1:
                return True


