class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 0
        k = 0
        t = 3
        while k < n:
            i += 1
            k += t
            t += 2
        return i