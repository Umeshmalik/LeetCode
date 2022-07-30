class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d = {}
        for word in words2:
            t = {}
            for i in word:
                t[i] = t[i] + 1 if i in t else 1
            for i in t.keys():
                d[i] = max(d[i], t[i]) if i in d else t[i]
        arr = []
        print(d)
        for word in words1:
            di = {}
            is_there = True
            for w in word:
                di[w] = di[w] + 1 if w in di else 1
            for i in d.keys():
                if i not in di or d[i] > di[i]:
                    is_there = False
                    break
            if is_there:
                arr.append(word)
        return arr