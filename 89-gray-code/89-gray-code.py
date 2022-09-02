class Solution:
    def grayCode(self, n: int) -> List[int]:
        diff = [int(math.pow(2, i)) for i in range(n)]
        res = [0]
        for i in diff:
            res += [i + j for j in reversed(res)]
        return res