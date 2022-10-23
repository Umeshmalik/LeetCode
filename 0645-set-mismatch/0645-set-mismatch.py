class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mp = set()
        dup = miss = -1
        for i in nums:
            if i in mp:
                dup = i
            mp.add(i)
        for i in range(1, len(nums)+1):
            if i not in mp:
                miss = i
                break
        return [dup, miss]