class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        last = 0
        for i in arr:
            count += (i - last - 1)
            if count >= k:
                return i - (count - k + 1)
            last = i
        return arr.pop() + (k - count)