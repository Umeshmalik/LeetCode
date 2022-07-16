class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for n in range(len(nums)):
            if nums[n] in d:
                d[nums[n]] =n
            else:
                d[nums[n]] = n
        for n in range(len(nums)):
            remain = target - nums[n]
            if remain in d and d[remain] != n:
                return [n,d[remain]]