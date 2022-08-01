class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        arr = [[1]*len(obstacleGrid[0])]*len(obstacleGrid)
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    arr[i][j] = 0
                elif i == 0:
                    arr[i][j] = arr[i][j-1]
                elif j == 0:
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i][j-1] + arr[i-1][j]
        return arr[-1][-1]