class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = collections.Counter(magazine)
        for i in ransomNote:
            if i not in d:
                return False
            elif d[i] == 1:
                del d[i]
            else:
                d[i] -= 1
        return True