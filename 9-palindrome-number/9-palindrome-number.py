class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        x = str(x)
        for i in range(0, len(x)//2):
            if x[i] != x[len(x)-i-1]: return False
        return True