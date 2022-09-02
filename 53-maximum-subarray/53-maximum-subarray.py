class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) <= 0: return max(nums)
        curr = sm = 0
        for i in nums:
            curr += i
            if curr > sm:
                sm = curr
            elif curr < 0:
                curr = 0
        return sm