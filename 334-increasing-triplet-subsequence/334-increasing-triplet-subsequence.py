class Solution:
    def increasingTriplet(self, arr: List[int]) -> bool:
        def bisect_left(ls, n):
            le = len(ls)
            if le == 1: return 0
            elif le == 2 and n <= ls[0]:
                return 0
            elif le == 2 and n <= ls[1]:
                return 1
        dp = [arr[0]]
        for i, n in enumerate(arr[1:]):
            if dp[-1] < n:
                dp.append(n)
                if len(dp) > 2: return True
            else:
                dp[bisect_left(dp, n)] = n
        return False if len(dp) < 3 else True