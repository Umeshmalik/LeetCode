class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = prices.pop(0)
        for i in prices:
            mn = min(i, mn)
            ans = max(ans, i - mn)
        return ans