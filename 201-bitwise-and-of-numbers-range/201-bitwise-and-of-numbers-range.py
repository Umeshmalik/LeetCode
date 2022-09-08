class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        binA, binB = bin(left)[2:], bin(right)[2:]
        if len(binA) != len(binB): return 0
        res = ""
        for i in range(len(binA)):
            if binA[i] == binB[i]: res += binA[i]
            else:
                res += ("0" * (len(binA) - i))
                break
        return int(res, 2)