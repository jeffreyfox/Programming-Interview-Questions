# TAGS:binary search

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# classic binary search
class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
        