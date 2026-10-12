class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n & (n-1)
            count += 1

        return count
        #we'll have sequence of 0s at last only and only if no 1 was there in last n-1
