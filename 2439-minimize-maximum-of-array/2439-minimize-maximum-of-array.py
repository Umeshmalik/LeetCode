class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = current_result = 0
        for i in range(len(nums)):
            current_result+= nums[i]
            result= max(result, (current_result+ i)// (i+ 1))
        return result