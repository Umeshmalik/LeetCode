from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = Counter(Counter(arr).values()).values()
        for i in arr:
            if i != 1: return False
        return True
        
            