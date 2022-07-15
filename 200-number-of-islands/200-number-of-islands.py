class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        curr = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    curr += 1
                    self.getMax(i, j, grid)
        return curr
    
    def getMax(self, a, b, grid):
        if  a < 0 or b < 0 or a >= len(grid) or b >= len(grid[0]) or grid[a][b] == "0":
            return
        grid[a][b] = "0"
        self.getMax(a-1, b, grid)
        self.getMax(a, b-1, grid)
        self.getMax(a, b+1, grid)   
        self.getMax(a+1, b, grid)
        return