class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        arr = []
        while n:
            arr.append(n%3)
            n //= 3
        for i in arr:
            if i == 2:
                return False
        return True