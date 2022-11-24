from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedList = SortedList(nums)
        res = []
        print(sortedList)
        print(nums)
        for n in nums:
            res.append(sortedList.index(n))
            sortedList.remove(n)
        return res