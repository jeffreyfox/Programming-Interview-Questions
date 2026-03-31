# Two passes. Get max and then compare

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_count = 0
        for c in candies:
            max_count = max(max_count, c)
        result = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_count:
                result[i] = True
        return result

# cleaner solution
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_count = max(candies)
        return [c + extraCandies >= max_count for c in candies]