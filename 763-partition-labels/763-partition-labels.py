class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]] = [i, i]
            else:
                hm[s[i]][1] = max(hm[s[i]][1], i)
                hm[s[i]][0] = min(hm[s[i]][0], i)
        res = []
        i = 0
        while(i < len(s)):
            mn = hm[s[i]][0]
            mx = hm[s[i]][1]
            j = mn + 1
            while(j <= mx):
                if hm[s[j]][1] > mx:
                    mx = hm[s[j]][1]
                j += 1
            res.append(mx - mn + 1)
            i = mx + 1
        return res