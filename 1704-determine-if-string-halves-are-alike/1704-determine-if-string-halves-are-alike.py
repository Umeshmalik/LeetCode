class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        arr = ['a', 'A', 'i', 'I', 'e', 'E', 'o', 'O', 'u', 'U']
        firstH = secondH = 0
        size = len(s)
        for i in range(size//2):
            if s[i] in arr:
                firstH += 1
        for i in range(size//2, size):
            if s[i] in arr:
                secondH += 1
        return secondH == firstH