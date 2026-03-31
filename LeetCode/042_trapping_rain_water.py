# TAGS: array,greedy,DP
# Calculates the total trapped rain water using a Two-Pointer approach.
    
# The algorithm maintains two pointers (left and right) and their respective 
# maximum heights encountered so far. By always moving the pointer with the 
# smaller maximum height, we can guarantee that the 'bottleneck' for water 
# retention is known, allowing us to calculate the trapped water at each 
# step in a single pass.
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        water = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water += max_right - height[right]
        return water