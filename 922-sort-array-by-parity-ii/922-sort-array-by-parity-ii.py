class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd , even = 1 , 0
        while odd < len(nums) and even < len(nums):
            while odd < len(nums) and nums[odd] % 2 != 0:
                odd += 2
            while even < len(nums) and nums[even] % 2 == 0:
                even += 2
            if odd < len(nums) and even < len(nums):
                nums[even], nums[odd] = nums[odd], nums[even]
                odd, even = odd + 2, even + 2
        return nums;