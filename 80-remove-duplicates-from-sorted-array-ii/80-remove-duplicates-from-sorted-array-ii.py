class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 2
        while right < len(nums):
            if nums[right] == nums[left-2]:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
        return left