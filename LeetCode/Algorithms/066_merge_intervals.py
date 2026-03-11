# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# Sort the intervals by the starting time. Then merge the intervals if they are overlapping.
# We can further simplify the is_overlap and get_merged functions because the list is already sorted.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: (x[0], x[1]))

        def is_overlap(a: List[int], b: List[int]):
            return a[0] <= b[1] and b[0] <= a[1]

        def get_merged(a: List[int], b: List[int]):
            return [min(a[0], b[0]), max(a[1], b[1])]

        result = [intervals[0]]
        for curr in intervals[1:]:
            last = result[-1]
            if is_overlap(curr, last):
                result[-1] = get_merged(curr, last)
            else:
                result.append(curr)
            
        return result


