class Solution:
    def increasingTriplet(self, arr: List[int]) -> bool:
        def bisect_left(list, n):
            lo = 0
            hi = len(list)
            while lo < hi:
                mid = (lo + hi) >> 1
                if list[mid] < n:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        dp = [arr[0]]
        for i, n in enumerate(arr[1:]):
            if len(dp) > 2: return True
            if dp[-1] < n:
                dp.append(n)
            else:
                dp[bisect_left(dp, n)] = n
        return False if len(dp) < 3 else True