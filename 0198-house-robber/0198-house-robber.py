class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        arr = [nums[0], nums[1]]
        arr.append(nums[0]+nums[2])
        for i in range(3, len(nums)):
            arr.append(nums[i] + max(arr[i-2], arr[i - 3]))
        return max(arr[-1], arr[-2])