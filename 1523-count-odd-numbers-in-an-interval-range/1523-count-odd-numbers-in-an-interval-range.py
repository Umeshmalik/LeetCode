class Solution:
    def countOdds(self, low: int, high: int) -> int:
         return ((high-low)>>1) + (1 if (low&1 or high&1) else 0);