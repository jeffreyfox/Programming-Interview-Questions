# Solution using heapq (priority queue). Use negative to minic a max queue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-v for v in nums]
        heapq.heapify(arr)
        res = 0
        for _ in range(k):
            heapq.heappop(arr)
        return -arr[0]

# Solution using min heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        return nums[0]