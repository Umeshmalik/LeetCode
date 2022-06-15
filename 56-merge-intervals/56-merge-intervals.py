class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        i = 0
        while(i < len(intervals)):
            j, k = i, i + 1
            mx = intervals[i][1]
            mi = intervals[i][0]
            while(k < len(intervals) and (mx >= intervals[k][0])):
                mx = max(mx, intervals[k][1])
                mi = min(mi, intervals[k][0])
                j += 1
                k += 1
            res.append([mi, mx])
            i = j + 1
        return res