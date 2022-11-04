class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [*s]
        start, end = 0, len(s) - 1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        while start < end:
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif s[start] in vowels:
                end -= 1
            elif s[end] in vowels:
                start += 1
            else:
                start += 1
                end -= 1
        return "".join(s)