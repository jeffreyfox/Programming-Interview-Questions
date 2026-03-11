# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Solution using a dummy head.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            tot = v1 + v2 + carry
            carry = tot // 10
            tot = tot % 10
            curr.next = ListNode(tot)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next

# Solution without a dummy head.
lass Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        root = None
        prev = None
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            carry = sum // 10
            sum = sum % 10
            node = ListNode(sum)
            if prev:
                prev.next = node
            else:
                root = node
            prev = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            prev.next = ListNode(carry)

        return root
