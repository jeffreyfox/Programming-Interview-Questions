# Use prefix DP where minCuts[i] is the minimum cuts for s[0:i).

# Expand around each center to enumerate all palindromes, and whenever palindrome s[left:right+1] is found, update minCuts[right+1] from minCuts[left] + 1.

from math import inf

class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0
    
        n = len(s)

        # minCuts[i] = minimum cuts needed for prefix s[0:i]
        minCuts = [inf] * (n + 1)

        # sentinel value so a full-prefix palindrome gives 0 cuts
        minCuts[0] = -1

        for i in range(n):

            # expand around i for odd-length palindromes
            j = 0
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                # palindrome s[i-j : i+j]
                minCuts[i + j + 1] = min(minCuts[i + j + 1], minCuts[i - j] + 1)
                j += 1

            # expand around (i, i+1) for even-length palindromes
            j = 0
            while i - j >= 0 and i + j + 1 < n and s[i - j] == s[i + j + 1]:
                # palindrome s[i-j : i+j+1]
                minCuts[i + j + 2] = min(minCuts[i + j + 2], minCuts[i - j] + 1)
                j += 1
        
        return minCuts[n]