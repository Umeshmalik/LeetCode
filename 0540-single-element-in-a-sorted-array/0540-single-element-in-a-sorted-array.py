class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans