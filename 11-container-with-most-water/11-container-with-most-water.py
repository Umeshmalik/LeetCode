class Solution:
    def maxArea(self, a: List[int]) -> int:
        mx , lf, rg = 0, 0, len(a)-1
        while lf < rg:
            if a[lf] < a[rg]:
                res = a[lf]*(rg-lf)
                lf += 1
            else:
                res = a[rg]*(rg-lf)
                rg -= 1
            if res > mx: mx = res
        return mx