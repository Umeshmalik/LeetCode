class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start , end = 0, len(nums) - 1
        while start <= end:
            mid = (end + start)//2
            if nums[mid] == target:
                l = r = mid
                while l >= 0 and nums[l] == target: l -= 1
                while r < len(nums) and nums[r] == target: r += 1
                return [l+1, r-1]
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return [-1, -1]