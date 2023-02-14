class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ""
        lenA = len(a)-1
        lenB = len(b)-1
        while lenA >= 0 and lenB >= 0:
            sm = int(a[lenA]) + int(b[lenB]) + carry
            ans  = str(sm%2) + ans
            carry = sm//2
            lenA -= 1
            lenB -= 1

        while lenA >= 0:
            sm = int(a[lenA]) + carry
            ans = str(sm%2) + ans
            carry = sm//2
            lenA -= 1

        while lenB >= 0:
            sm = int(b[lenB]) + carry
            ans = str(sm%2) + ans
            carry = sm//2
            lenB -= 1

        if carry == 1:
            ans = "1" + ans
        return ans