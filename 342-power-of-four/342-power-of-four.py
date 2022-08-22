class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0: return False
        bn = bin(n)
        one = False
        zero = 0
        for i in range(len(bn)):
            if one and bn[i] == '0':
                zero += 1
            if one and bn[i] == '1':
                return False
            if not one and bn[i] == '1':
                one = True
        return True if one and zero % 2 == 0 else False