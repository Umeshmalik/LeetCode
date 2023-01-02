class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        isCap = False
        isSmall = False
        for i in word[1:]:
            if 'A' <= i <= 'Z':
                isCap = True
            if 'a' <= i <= 'z':
                isSmall = True
        if isCap and isSmall: return False
        if isCap and 'a' <= word[0] <= 'z': return False
        return True