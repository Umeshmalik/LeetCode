class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        n = len(nums)
        while j < n:
            t = nums[j]
            while j < n and nums[j] == t: j += 1
            nums[i] = t
            i += 1
        return i