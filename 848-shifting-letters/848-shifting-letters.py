class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2 , -1, -1):
            shifts[i] += shifts[i+1]
        for i in range(len(s)):
            s = s[:i] + chr((((ord(s[i]) + shifts[i]) - ord('a'))%26) + ord('a')) + s[i + 1:] 
        return s