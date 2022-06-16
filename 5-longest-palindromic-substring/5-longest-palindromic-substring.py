class Solution:
    def longestPalindrome(self, s: str) -> str:
        st = s[0]
        for i in range(len(s)):
            mn = i-1
            mx = i+1
            while( mn >= 0 and mx < len(s) and s[mn] == s[mx]):
                mn , mx = mn - 1, mx + 1
            if ( (mx - 1) - (mn + 1) + 1 > len(st)):
                st = s[mn+1: mx]
            mn = i
            mx = i+1
            while( mn >= 0 and mx < len(s) and s[mn] == s[mx]):
                mn , mx = mn - 1, mx + 1
            if ( mx - mn > len(st)):
                st = s[mn+1: mx]
        return st