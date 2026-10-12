class Solution:
    def countBits(self, n: int) -> List[int]:
        

        def ones(n):
            count = 0
            while n != 0:
                n = n & (n-1)
                count += 1

            return count

        arr = []
        for i in range(n+1):
            arr.append(ones(i))

        return arr