class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        res = sys.maxsize
        for r in range(len(nums)):
            sum += nums[r]
            if(sum >= target):
                while sum >= target:
                    sum -= nums[l]
                    l += 1
                res = min(res, r - l +2)
        return res if res != sys.maxsize else 0