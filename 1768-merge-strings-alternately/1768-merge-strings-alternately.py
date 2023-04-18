class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join((a+b) for a, b in zip(word1, word2)) + word1[min(len(word1), len(word2)):] + word2[min(len(word1), len(word2)):]