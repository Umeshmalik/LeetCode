class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = collections.Counter(arr)
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