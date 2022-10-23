class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        mat = nums
        for k in range(1, len(nums)):
            for j in range(len(nums)-1):
                mat[j] = (nums[j] + mat[j+1])%10
            mat.pop()
            nums = mat
        return mat[-1]