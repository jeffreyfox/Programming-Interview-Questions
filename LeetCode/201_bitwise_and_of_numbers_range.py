# TAGS: bit

# Keep shifting left and right left until they are equal (to get the common left prefix)
# track the number of shifts
# Then shift the final number back
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left < right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count