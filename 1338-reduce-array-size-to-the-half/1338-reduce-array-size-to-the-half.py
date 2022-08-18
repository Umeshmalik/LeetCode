class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            d[i] = 1 if i not in d else d[i] + 1
        size = len(arr)
        li = sorted(list(d.values()))
        s = 0
        k = 0
        for i in range(len(li)-1, -1, -1):
            s += li[i]
            k += 1
            if s >= size//2:
                break
        return k