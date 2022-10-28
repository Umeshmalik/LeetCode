class Solution:
    def longestPrefix(self, s: str) -> str:
        ans = ""
        size = len(s)
        for i in range(1, size):
            frontStr = s[:i]
            if frontStr == s[size - i:]:
                ans = frontStr if len(frontStr) > len(ans) else ans
        return ans