class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1: return 1
        d = {}
        for i, j in trust:
            d[j] = d[j] + 1  if j in d else 1
        peo = []
        for i in d.keys():
            if d[i] == n - 1:
                peo.append(i)
        for i, j in trust:
            if i in peo:
                peo.remove(i)
        return -1 if len(peo) == 0 else peo[0]