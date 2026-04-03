# TAGS: string,math

# Solution using math
# A valid gcd string must satisfy two things:
# - Both strings are made by repeating the same base pattern.
# - The longest such pattern must have length gcd(len(str1), len(str2)).
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If they are built from the same base pattern,
        # concatenating in either order should give the same result.
        if str1 + str2 != str2 + str1:
            return ""
        
        return str1[:gcd(len(str1), len(str2))]

# Brute-force solution:
# Any valid "gcd string" must be a prefix of the shorter string.
# We try all prefixes of the shorter string from longest to shortest.
#
# For each candidate prefix:
#   - Check if it can be repeated to form str1
#   - Check if it can be repeated to form str2
#
# The first valid candidate (longest) is the answer.
#
# Time: O(min(m, n) * (m + n))
# Space: O(m + n) due to temporary string construction

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def divides(s: str, pattern: str) -> bool:
            if len(s) % len(pattern) != 0:
                return False
            return s == pattern * (len(s) // len(pattern))

        shorter = str1 if len(str1) <= len(str2) else str2

        for i in range(len(shorter), 0, -1):
            candidate = shorter[:i]
            if divides(str1, candidate) and divides(str2, candidate):
                return candidate

        return ""