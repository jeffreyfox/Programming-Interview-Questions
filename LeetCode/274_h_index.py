# My solution using counting
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0] * 1001
        for c in citations:
            counts[c] += 1
        for i in range(1000-1, -1, -1):
            counts[i] += counts[i+1]
        for i in range(1000, -1, -1):
            if counts[i] >= i:
                return i
        return 0

# ChatGPT optimized solution:
# Count how many papers have each citation count, convert it into
# "papers with at least i citations" via suffix sums, then scan from
# high to low to find the largest h where count >= h.
# Works for LC constraints, though using a fixed 1001-sized array is
# less general than the usual n+1 bucket approach.
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0] * (n + 1)

        for c in citations:
            counts[min(c, n)] += 1

        papers = 0
        for h in range(n, -1, -1):
            papers += counts[h]   # papers with at least h citations
            if papers >= h:
                return h

        return 0