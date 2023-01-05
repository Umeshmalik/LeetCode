class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        mx = points[0][1]
        dartRequired = 1
        for i in range(len(points)):
            if points[i][0] > mx:
                dartRequired += 1
                mx = max(mx, points[i][1]);
        return dartRequired