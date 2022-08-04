class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        LCM = lcm(p,q)
        if (LCM//q) % 2 == 0: return 2
        return (LCM//p) % 2