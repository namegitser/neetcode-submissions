class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        sys.setrecursionlimit(len(nums) + 100)
        memo = {}
        # Global variable to track the highest positive product seen anywhere
        self.global_max = nums[0]

        def dfs(i):
            # Base Case: The very first number has no past history
            # print(nums[i])
            if i == 0:
                return nums[0], nums[0]
            
            # Caching check
            if i in memo:
                return memo[i]

            # 1. Ask the row behind us for its max and min histories
            prev_max, prev_min = dfs(i - 1)
            current_num = nums[i]

            # 2. The 3-way Contiguous Choice Contenders
            cand1 = current_num
            cand2 = current_num * prev_max
            cand3 = current_num * prev_min
            # print(f'curr candidates - {cand1}, {cand2}, {cand3}')

            # 3. Compute the current states
            curr_max = max(cand1, cand2, cand3)
            curr_min = min(cand1, cand2, cand3)

            # 4. Update our master overall record holder
            self.global_max = max(self.global_max, curr_max)

            # 5. Cache and return both states together
            memo[i] = (curr_max, curr_min)
            return memo[i]

        # Kick off recursion starting at the very last index of the array
        dfs(len(nums) - 1)
        return self.global_max
