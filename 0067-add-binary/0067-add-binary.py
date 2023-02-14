class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = []
        lenA = len(a)-1
        lenB = len(b)-1
        while lenA >= 0 and lenB >= 0:
            sm = int(a[lenA]) + int(b[lenB]) + carry
            ans.insert(0, str(sm%2))
            carry = sm//2
            lenA -= 1
            lenB -= 1

        while lenA >= 0:
            sm = int(a[lenA]) + carry
            ans.insert(0, str(sm%2))
            carry = sm//2
            lenA -= 1

        while lenB >= 0:
            sm = int(b[lenB]) + carry
            ans.insert(0, str(sm%2))
            carry = sm//2
            lenB -= 1

        if carry == 1:
            ans.insert(0, "1")
        return "".join(ans)