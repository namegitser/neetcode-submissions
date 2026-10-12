class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # 1. Make room in res by shifting left
            res = (res << 1)
            # 2. Extract the rightmost bit of n and add it to res
            res = res | (n & 1)
            # 3. Shift n right to process the next bit
            n = n >> 1
        return res
