# TAGS: bit

# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

# Example 1:

# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128

# Output: 1

# Explanation:

# The input binary string 10000000 has a total of one set bit.

# Example 3:

# Input: n = 2147483645

# Output: 30

# Explanation:

# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

# Constraints:

# 1 <= n <= 231 - 1

# Solution 1. Scan each bit
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
        return count

# A more elegant solution by keep unsetting the rightmost set bit
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count

# Similar approach by keep unsetting the leftmost set bit
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n = n ^ (1 << (n.bit_length()-1))
            ans += 1
        return ans        