class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right: return left
        countA = countB = 0
        A, B = left, right
        while A:
            A >>= 1
            countA += 1
        while B:
            B >>= 1
            countB += 1
        if countA != countB: return 0
        res = left
        for i in range(left+1, right+1): res &= i
        return res