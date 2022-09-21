class Solution:
    def tribonacci(self, n: int) -> int:
        x1 = 0
        x2 = x3 = 1
        if n == 0: return 0
        if n in [1,2] : return 1
        for i in range(3, n+1):
            t = x1 + x2 + x3
            x1 = x2
            x2 = x3
            x3 = t
        return x3