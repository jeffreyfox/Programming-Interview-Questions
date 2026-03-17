# TAGS: bit

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n == (n & -n)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

