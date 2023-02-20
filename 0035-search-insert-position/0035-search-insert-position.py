class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target or nums[mid] > target > nums[mid-1]:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start