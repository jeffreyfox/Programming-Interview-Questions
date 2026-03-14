# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: true
 

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti < endi <= 106
 
# Solution using sorting and linear scan
# Time complexity: O(n log n)
# Space complexity: O(1)
# Note how we check for overlap between adjacent intervals. We don't need to 
# check a[0] < b[1] because the intervals are already sorted by start time.
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort()
        for i in range(len(intervals)-1):
            a = intervals[i]
            b = intervals[i+1]
            if a[1] > b[0]:
                return False
        return True