from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([b*a for a, b in sorted(Counter(s).items(), key = lambda char: char[1], reverse=True)])