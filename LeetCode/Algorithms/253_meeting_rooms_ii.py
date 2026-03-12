# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106


# Solution using sweep line algorithm
# Use a list of tuple. Note that we mark the closing event as 0 so it will come first after sorting
# Then we iterate through the list and count the number of rooms needed
# The maximum number of rooms needed is the answer
# This is a greedy algorithm
# Time complexity: O(n log n)
# Space complexity: O(n)
# Also note how we iterate through the list to get the individual elements in the tuple

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        # mark closing event as 0 so it will come first after sorting
        for start, end in intervals:
            events.append([start, 1])
            events.append([end, 0])
        events.sort()
        rooms = 0
        max_rooms = 0
        for _, typ in events:
            if typ == 1:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
            else:
                rooms -= 1
        return max_rooms
