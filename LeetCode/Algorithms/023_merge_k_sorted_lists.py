# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution using a min-oriented priority queue.
# Two tricks:
# 1. Use a tie-breaker index in the heap tuple (val, idx, node) to prevent Python from trying to
#    compare ListNode objects when values are equal.
# 2. Reuse the existing linked-list nodes (curr.next = node) instead of creating new nodes, 
#    which avoids unnecessary allocations and keeps the solution cleaner.
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, head in enumerate(lists):
            if head is None:
                continue
            heapq.heappush(heap, (head.val, idx, head))

        dummy = ListNode(-1)
        curr = dummy
        while heap:
            _, idx, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
            
        return dummy.next