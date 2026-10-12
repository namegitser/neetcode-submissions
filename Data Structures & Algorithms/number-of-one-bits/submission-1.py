class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            if n % 2 == 1:
                count += 1

            n = n >> 1

        return count
        #TC - O(32)->O(1)
        #Mem - O(1)
        #But it also checks all intermediate 0 -> 1000000011 