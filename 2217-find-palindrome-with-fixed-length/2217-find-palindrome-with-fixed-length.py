class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        arr = []
        if intLength % 2 == 0:
            start, end = 10 ** ((intLength // 2) - 1), 10 ** (intLength // 2) - 1
            for i in queries:
                n = str(start + i - 1) + str(start+i-1)[::-1]
                if len(n) > intLength:
                    n = -1
                arr.append(int(n))
        else:
            start, end = 10 ** ((intLength // 2) - 1), 10 ** (intLength // 2) - 1
            if intLength == 1:
                for i in queries:
                    n = -1 if i > 9 else i
                    arr.append(n)
                return arr
            for i in queries:
                i -= 1
                n = str(start+i//10) + str((i % 10)) + str(start+i//10)[::-1]
                if len(n) > intLength:
                    n = -1
                arr.append(int(n))
        return arr