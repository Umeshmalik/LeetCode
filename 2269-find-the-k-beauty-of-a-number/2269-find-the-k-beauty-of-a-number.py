class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        st = str(num)
        for i in range(len(st) - k+1):
            if int(st[i:i+k]) and not num % int(st[i:i+k]): 
                ans += 1
        return ans