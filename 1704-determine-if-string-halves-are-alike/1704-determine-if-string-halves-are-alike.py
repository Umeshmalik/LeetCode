class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        arr = ['a', 'A', 'i', 'I', 'e', 'E', 'o', 'O', 'u', 'U']
        firstH = secondH = 0
        size = len(s)
        i = 0
        for i in range(size):
            if s[i] in arr and i < size//2:
                firstH += 1
            elif s[i] in arr and i < size:
                secondH += 1
        return secondH == firstH