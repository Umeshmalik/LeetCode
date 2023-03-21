class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr = 0
        ans = 0
        for i in nums:
            if i == 0:
                curr += 1
            else:
                ans += ((curr+1)*curr//2)
                curr = 0
        ans += ((curr+1)*curr//2)
        return ans