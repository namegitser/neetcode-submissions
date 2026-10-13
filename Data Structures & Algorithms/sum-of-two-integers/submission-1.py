class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to restrict numbers to 32 bits (4 bytes)
        mask = 0xFFFFFFFF
        # The largest positive integer in 32-bit signed systems
        max_int = 0x7FFFFFFF
        # print(bin(mask), bin(max_int))
        while b != 0:
            # 1. Find the carry bits and restrict to 32 bits
            carry = (a & b) & mask
            # 2. Add bits without carry and restrict to 32 bits
            a = (a ^ b) & mask
            # 3. Shift the carry left by 1 bit and restrict to 32 bits
            b = (carry << 1) & mask

        # If 'a' exceeds max_int, it means it is a negative number in 32-bit logic
        return a if a <= max_int else ~(a ^ mask)