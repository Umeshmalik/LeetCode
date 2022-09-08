class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right: return left
        in_range = False
        for i in range(32):
            if 2 ** i < right and 2 ** i > left:
                return 0
            if 2 ** i <= left and 2 ** (i+1) >= right:
                in_range = True
        if in_range:
            ans = left
            for i in range(left+1, right+1):
                ans &= i
            return ans
        return 0