class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        mx = len(nums) // 3
        ans = []
        for i in d.keys():
            if d[i] > mx:
                ans.append(i)
        return ans