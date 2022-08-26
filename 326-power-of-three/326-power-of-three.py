class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False
        arr = []
        while n:
            arr.append(n%3)
            n //= 3 
        is_valid = False
        for i in arr:
            if (is_valid and (i == 1 or i == 2)) or i == 2:
                return False
            if i == 1:
                is_valid = True
        return is_valid