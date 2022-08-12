class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        k = max(len(num1), len(num2))
        arr = [""] * (k + 1)
        carry = 0
        while i >= 0 and j >= 0:
            su = int(num1[i]) + int(num2[j]) + carry
            carry = su // 10
            arr[k] = str(su % 10)
            k -= 1
            i -= 1
            j -= 1
        if j >= 0:
            while j >= 0:
                su = int(num2[j]) + carry
                carry = su // 10
                arr[k] = str(su % 10)
                k -= 1
                j -= 1
        if i >= 0:
            while i >= 0:
                su = int(num1[i]) + carry
                carry = su // 10
                arr[k] = str(su % 10)
                k -= 1
                i -= 1
        if carry > 0:
            arr[k] = str(carry)
        return "".join(arr)