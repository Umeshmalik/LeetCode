import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for i in range(len(nums)):
            heapq.heappush(arr, nums[i])
            if len(arr) > k:
                heapq.heappop(arr)
        return heapq.heappop(arr)