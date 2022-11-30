from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return max(list(Counter(Counter(Counter(arr).values()).values()).keys())) == 1
            