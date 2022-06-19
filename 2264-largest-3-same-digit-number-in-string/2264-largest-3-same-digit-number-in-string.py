class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s = ""
        for i in range( 2, len(num)):
            if num[i] == num[i-1] and num[i] == num[i-2]:
                s = num[i-2:i+1] if num[i] > s else s
        return s