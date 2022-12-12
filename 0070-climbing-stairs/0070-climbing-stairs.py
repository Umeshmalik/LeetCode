class Solution:
    def climbStairs(self, n: int) -> int:
        o, t = 1, 2
        for i in range(2, n): o, t = t, o + t
        return t if n > 1 else 1
            