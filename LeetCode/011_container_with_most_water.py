# TAGS: two pointers,greedy

# Use two pointers. The area is limited by the shorter line,
# so move the pointer at the shorter line to try to find a taller one.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        max_area = 0
        while lo < hi:
            max_area = max(max_area, (hi - lo) * min(height[lo], height[hi]))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return max_area