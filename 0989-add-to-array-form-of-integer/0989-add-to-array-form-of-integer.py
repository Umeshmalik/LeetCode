class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        b = str(k)
        carry = 0
        ans = ""
        lenA = len(num)-1
        lenB = len(b)-1
        while lenA >= 0 and lenB >= 0:
            sm = num[lenA] + int(b[lenB]) + carry
            ans  = str(sm%10) + ans
            carry = sm//10
            lenA -= 1
            lenB -= 1

        while lenA >= 0:
            sm = num[lenA] + carry
            ans = str(sm%10) + ans
            carry = sm//10
            lenA -= 1

        while lenB >= 0:
            sm = int(b[lenB]) + carry
            ans = str(sm%10) + ans
            carry = sm//10
            lenB -= 1

        if carry == 1:
            ans = "1" + ans
        return [int(i) for i in ans]