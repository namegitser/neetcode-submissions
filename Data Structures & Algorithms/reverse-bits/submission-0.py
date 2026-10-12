class Solution:
    def reverseBits(self, n: int) -> int:
        # Step 1: Extract bits from right to left into a string.
        # Because we read 'n' from right to left but append to the string from left to right,
        # the string 'binary' ends up naturally reversed!
        binary = ""
        for i in range(32):
            # (1 << i) creates a bitmask targeting the i-th bit position.
            # n & bitmask checks if that specific bit is set to 1.
            if n & (1 << i) != 0:
                binary += "1"
            else:
                binary += "0"
        
        # Step 2: Reconstruct the number from the reversed string.
        res = 0
        # Iterate from left to right through the already-reversed string.
        # enumerate gives us the correct target bit index 'i' (0 to 31).
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                # Use bitwise OR to set the i-th bit of the result to 1
                res = res | (1 << i)

        return res
