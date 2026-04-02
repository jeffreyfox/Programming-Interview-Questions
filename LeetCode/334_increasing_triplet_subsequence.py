# TAGS: greedy,array

# Greedy O(n) solution:
# Track two values:
#   first  = smallest number seen so far
#   second = smallest number that can form an increasing pair with first
#
# For each number x:
#   - if x <= first: update first
#   - elif x <= second: update second (we found a better pair)
#   - else: x > second → found first < second < x → return True
#
# Key insight:
# We only need to track the existence of a valid increasing pair, not the exact indices.
# Even if first gets updated later, second still represents a valid earlier pair.
#
# Time: O(n)
# Space: O(1)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = None
        for x in nums:
            if first is None or x <= first:
                first = x
            elif second is None or x <= second:
                second = x
            else:
                return True
        return False

# Solution without using the inf trick
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = None
        for x in nums:
            if first is None or x <= first:
                first = x
            elif second is None or x <= second:
                second = x
            else:
                return True
        return False