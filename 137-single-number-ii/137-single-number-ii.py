class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = [0]*32
        negCount = 0
        for i in nums:
            s = bin(i)[2:] if bin(i)[0] != '-' else bin(i)[3:]
            if bin(i)[0] == '-':
                negCount += 1
            for j in range(len(s)-1, -1, -1):
                res[31 - len(s) + j + 1] += int(s[j])
        ans = 0
        for i in range(32):
            if res[31- i] % 3 == 1:
                ans += (2 ** i)
        return -ans if negCount%3 == 1 else ans