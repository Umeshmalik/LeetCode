class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 1 or len(nums) == 1: return max(nums)
        currMax = currMin = maxYet = minYet = nums[0]
        for i in nums[1:]:
            currMax = max(currMax+i, i)
            maxYet = max(maxYet, currMax)
            
            currMin = min(currMin+i, i)
            minYet = min(minYet, currMin)
        return max(maxYet, sum(nums) - minYet)