from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([b*a for a, b in sorted([[key, Counter(s)[key]] for key in Counter(s)], key = lambda char: char[1], reverse=True)])