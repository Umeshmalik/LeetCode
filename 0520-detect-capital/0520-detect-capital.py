class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        isCap = isSmall = False
        for i in word[1:]:
            if 'A' <= i <= 'Z':
                isCap = True
            if 'a' <= i <= 'z':
                isSmall = True
        return False if isCap and (isSmall or 'a' <= word[0] <= 'z') else True