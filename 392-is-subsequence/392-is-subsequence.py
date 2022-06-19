class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in t:
            if j == len(s):
                return True
            if s[j] == i:
                j += 1
        if j == len(s):
            return True
        return False