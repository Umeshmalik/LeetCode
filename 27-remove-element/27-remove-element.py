class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = j = 0
        size = len(nums)
        while j < size:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i