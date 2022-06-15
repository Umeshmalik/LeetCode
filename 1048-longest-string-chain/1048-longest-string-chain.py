class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        d = {}
        for i in words:
            d[i] = 1
            for j in range(len(i)):
                successor = i[:j] + i[j+1:]
                if successor in d:
                    d[i] = max(d[i], d[successor] + 1)
        return max(d.values())