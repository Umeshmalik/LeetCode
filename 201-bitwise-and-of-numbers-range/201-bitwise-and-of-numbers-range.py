class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        counta, countb = 0,0
        a, b = left, right
        if a == b: return b
        while a>0:
            a=a>>1
            counta+=1
        while b>0:
            b=b>>1
            countb+=1
        res = 0
        if counta<countb: return 0
        if countb == 0: return 0
        res = left
        if counta == countb:
            for i in range(left+1, right+1): res=res&i
            return res
        return 2**(countb-1)