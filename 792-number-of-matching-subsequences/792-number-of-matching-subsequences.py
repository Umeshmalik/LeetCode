class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = 0
        def isPresent(s, word):
            if not word: return True
            j = 0
            for i, a in enumerate(s):
                if j == len(word): return True
                if a == word[j]:
                    j += 1
            return j == len(word)
        notPresent = set()
        present = set()
        for k in words:
            if k in notPresent: continue
            if k in present:
                n += 1
                continue
            if isPresent(s, k):
                n += 1
                present.add(k)
            else:
                notPresent.add(k)
        return n