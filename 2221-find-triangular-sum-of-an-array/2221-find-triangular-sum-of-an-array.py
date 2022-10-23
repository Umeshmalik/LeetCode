class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        mat = nums
        i = len(nums) - 1
        for k in range(1, len(nums)):
            for j in range(i):
                mat[j] = (nums[j] + mat[j+1])%10
            mat.pop()
            nums = mat
            i -= 1
        return mat[-1]