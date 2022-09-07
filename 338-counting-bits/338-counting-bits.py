class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(0, n+1):
            k = i
            sm = 0
            for j in range(32):
                if k & 1 == 1:
                    sm += 1
                k >>= 1
            arr.append(sm)
        return arr