class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def solve(i, j):
            # 1. Base Case: If either string is completely exhausted, no match is possible.
            if i >= len(text1) or j >= len(text2):
                return 0

            # 2. Check Memo: Prevent redundant work by caching using specific position indices (i, j).
            if (i, j) in memo:
                return memo[(i, j)]

            # 3. Match Case: Both characters match! Advance both pointers and add 1 to the length.
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + solve(i + 1, j + 1)
            
            # 4. Mismatch Case: Branch out by skipping a character from text1 OR text2, caching the max result.
            else:
                memo[(i, j)] = max(solve(i + 1, j), solve(i, j + 1))
            
            # The memo table builds up as the recursive stack unwinds, finally returning the total for (0, 0)
            return memo[(i, j)]

        return solve(0, 0)
