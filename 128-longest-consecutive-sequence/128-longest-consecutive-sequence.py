class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums.sort()
        max_gap = 0
        j = 1
        N = len(nums)
        curr = 1
        while j < N:
            if nums[j] - 1 == nums[j - 1]:
                j += 1
                curr += 1
            elif nums[j] == nums[j-1]:
                j += 1
            else:
                max_gap = max(max_gap, curr)
                j += 1
                curr = 1
        max_gap = max(max_gap, curr)
        return max_gap