class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = 1 if i not in d else d[i] + 1
        for ind, ch in enumerate(s):
            if d[ch] == 1:
                return ind
        return -1