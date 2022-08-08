class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx , lf, rg = 0, 0, len(height)-1
        while lf < rg:
            te = min(height[lf], height[rg])
            mx = max(mx, te*(rg-lf))
            if height[lf] < height[rg]:
                lf += 1
            else:
                rg -= 1
        return mx