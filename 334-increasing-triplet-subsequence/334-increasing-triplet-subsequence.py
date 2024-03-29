class Solution:
    def increasingTriplet(self, arr: List[int]) -> bool:
        dp = [arr[0]]
        for i in range(1, len(arr)):
            n = arr[i]
            if dp[-1] < n:
                dp.append(n)
                if len(dp) > 2: return True
            else:
                if len(dp) == 1 or (len(dp) == 2 and n <= dp[0]):
                    dp[0] = n
                elif len(dp) == 2 and n <= dp[1]:
                    dp[1] = n
        return False