class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[1]*n]*m
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i][j-1] + arr[i-1][j]
        return arr[m-1][n-1]