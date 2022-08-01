class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = []
        for i in range(m):
            ar = []
            for j in range(n):
                if i == 0 or j == 0:
                    ar.append(1)
                else:
                    ar.append(0)
            arr.append(ar)
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i][j-1] + arr[i-1][j]
        return arr[m-1][n-1]