class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = 0
        for i in range(1, n+1):
            s = ((s << int(math.log(i, 2)+1)) + i) % ((10 ** 9) + 7)
        return s