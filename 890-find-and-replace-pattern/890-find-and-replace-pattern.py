class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            d = {}
            is_match = True
            for i, n in enumerate(word):
                if pattern[i] in d:
                    if d[pattern[i]] != n :
                        is_match = False
                        break
                else:
                    if n in d.values():
                        is_match = False
                        break
                    d[pattern[i]] = n
            if is_match:
                res.append(word)
        return res