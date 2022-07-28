class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            d[i] = 1 if i not in d else d[i] + 1
        for i in t:
            if i not in d:
                return False
            if d[i] == 1:
                del d[i]
            else:
                d[i] = d[i] - 1
        if not d: return True
        return False