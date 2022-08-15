class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = mp[s[-1]]
        for i in range(len(s)-2, -1, -1):
            n = mp[s[i]]
            if n < mp[s[i+1]]:
                res -= n
            else:
                res += n
        return res