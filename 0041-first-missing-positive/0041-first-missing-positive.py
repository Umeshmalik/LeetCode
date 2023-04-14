from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp = set(nums)
        for i in range(1, max(max(nums) + 2, 2)):
            if i not in mp: return i