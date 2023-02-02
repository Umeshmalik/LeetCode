class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {};
        for i, n in enumerate(order): mp[n] = i
        for i in range(1, len(words)):
            if len(words[i]) < len(words[i - 1]) and words[i - 1][: len(words[i])] == words[i]: return False
            for j in range(min(len(words[i]), len(words[i-1]))):
                char1 = words[i][j]
                char2 = words[i - 1][j]
                if mp[char1] < mp[char2]: return False
                elif char1 == char2: continue
                else: break
        return True