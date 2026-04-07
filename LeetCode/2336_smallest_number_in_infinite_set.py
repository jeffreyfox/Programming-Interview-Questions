# TAGS: heap,hash table

# Maintain two parts of the infinite set:
# 1) `lowest`: the smallest number not yet popped (implicit infinite tail)
# 2) `heap`: min-heap of numbers that were popped and later added back
#
# popSmallest():
#   - If heap is non-empty, pop from heap (smallest restored number)
#   - Otherwise, return `lowest` and increment it
#
# addBack(num):
#   - Only add if num < lowest (i.e., it was previously removed)
#   - Use a set to avoid duplicate entries in the heap
#
# Time: O(log n) for heap ops, O(1) otherwise

import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.lowest = 1
        self.heap = []
        self.heap_set = set()

    def popSmallest(self) -> int:
        if self.heap:
            v = heapq.heappop(self.heap)
            self.heap_set.remove(v)
            return v

        ans = self.lowest
        self.lowest += 1
        return ans

    def addBack(self, num: int) -> None:
        if num < self.lowest and num not in self.heap_set:
            heapq.heappush(self.heap, num)
            self.heap_set.add(num)