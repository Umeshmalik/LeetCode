class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        mx = len(nums) // 3
        for i in nums:
            d[i] += 1
        ans = []
        for num, count in d.items():
            if count > mx:
                ans.append(num)
        return ans