class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        isCap = isSmall = False
        for i in range(1, len(word)):
            if 'A' <= word[i] <= 'Z':
                isCap = True
            if 'a' <= word[i] <= 'z':
                isSmall = True
        return False if isCap and (isSmall or 'a' <= word[0] <= 'z') else True