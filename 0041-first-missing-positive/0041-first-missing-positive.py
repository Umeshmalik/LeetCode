from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp = set(nums)
        i = 1
        while i:
            if i not in mp: return i
            i += 1