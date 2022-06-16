class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        leftMax = -11
        leftCurr = 1
        rightMax = -11
        rightCurr = 1
        for i in range(len(nums)):
            leftCurr *= nums[i]
            leftMax = max(leftCurr, leftMax)
            if leftCurr == 0:
                leftCurr = 1
        for i in range(len(nums) - 1, -1, -1):
            rightCurr *= nums[i]
            rightMax = max(rightCurr, rightMax)
            if rightCurr == 0:
                rightCurr = 1
        return max(leftMax, rightMax)