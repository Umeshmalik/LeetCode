class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        sm = 0
        for i in range(1, int(math.sqrt(num))+1):
            if i == 1 or i * i == num:
                sm += i
            elif num % i == 0:
                sm += i + num // i
        return True if sm == num else False