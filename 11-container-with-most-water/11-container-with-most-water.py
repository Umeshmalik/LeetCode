class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx , lf, rg = 0, 0, len(height)-1
        while lf < rg:
            if height[lf] < height[rg]:
                mx = max(mx, height[lf]*(rg-lf))
                lf += 1
            else:
                mx = max(mx, height[rg]*(rg-lf))
                rg -= 1
        return mx