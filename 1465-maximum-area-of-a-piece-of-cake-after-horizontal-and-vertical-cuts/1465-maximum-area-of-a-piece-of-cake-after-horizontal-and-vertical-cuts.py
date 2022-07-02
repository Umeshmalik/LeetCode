class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        horizontalCuts.sort()
        vmax = 0
        for i in range(len(verticalCuts)-1, 0, -1):
            vmax = max(vmax, verticalCuts[i] - verticalCuts[i-1])
        hmax = 0
        for i in range(len(horizontalCuts)-1, 0, -1):
            hmax = max(hmax, horizontalCuts[i] - horizontalCuts[i-1])
        return (vmax * hmax)%(10**9 + 7)