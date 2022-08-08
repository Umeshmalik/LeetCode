class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        dp = [1] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            for j in range(i+1, len(arr)):
                if arr[i] < arr[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)