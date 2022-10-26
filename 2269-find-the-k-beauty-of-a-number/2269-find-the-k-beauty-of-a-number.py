class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        st = str(num)
        for i in range(len(st) - k+1):
            n = int(st[i:i+k])
            if n != 0 and num % n == 0:
                ans += 1
        return ans