class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            crt_pos = nums[i] - 1
            if nums[i] != nums[crt_pos]:
                nums[i], nums[crt_pos] = nums[crt_pos], nums[i]
            else:
                i += 1
        arr = []
        for j in range(len(nums)):
            if nums[j] != j + 1:
                arr.append(nums[j])
            
        return arr