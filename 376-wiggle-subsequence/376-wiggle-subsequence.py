class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        result = 1
        prev = 0
        
        for i in range(1, len(nums)):
            curr = nums[i] - nums[i - 1]
            if curr == 0:
                continue
            elif prev == 0 or curr < 0 < prev or prev < 0 < curr:
                prev = curr
                result += 1

        return result