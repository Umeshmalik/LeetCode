class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        c = m = 0
        for i, j in properties:
            if j < m:
                c += 1
            m = max(m, j)
        return c